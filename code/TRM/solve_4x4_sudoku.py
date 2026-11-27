"""
Usage:
python solve_4x4_sudoku.py 0030000031404000 \
--config checkpoints/<data_path>/<run_name>/all_config.yaml \
--checkpoint checkpoints/<data_path>/<run_name>/step_<step_number>

Input digits use ordinary Sudoku notation: 0 or . means an empty cell.
The official TRM-style encoding is applied internally (raw cell value + 1).
"""

import argparse
import json
from pathlib import Path

import torch
import yaml

from utils.functions import load_model_class


def parse_puzzle(text: str) -> list[int]:
    cells = [c for c in text.strip() if c not in " \t\r\n|,+-"]
    cells = ["0" if c == "." else c for c in cells]
    if len(cells) != 16:
        raise ValueError(f"Expected 16 cells for a 4x4 Sudoku; got {len(cells)}.")
    if any(c not in "01234" for c in cells):
        raise ValueError("Cells must be 0-4, with 0 or . representing an empty cell.")
    return [int(c) for c in cells]


def latest_checkpoint(path: Path) -> Path:
    if path.is_file():
        return path
    candidates = []
    for candidate in path.glob("step_*"):
        suffix = candidate.name.removeprefix("step_")
        if suffix.isdigit():
            candidates.append((int(suffix), candidate))
    if not candidates:
        raise FileNotFoundError(f"No checkpoint file named step_<number> found in {path}")
    return max(candidates)[1]


def load_state_dict(path: Path, device: torch.device) -> dict:
    try:
        state = torch.load(path, map_location=device, weights_only=True)
    except TypeError:  # Older PyTorch versions
        state = torch.load(path, map_location=device)
    if isinstance(state, dict) and "state_dict" in state and isinstance(state["state_dict"], dict):
        state = state["state_dict"]
    if not isinstance(state, dict):
        raise TypeError(f"Checkpoint at {path} does not contain a state dictionary.")
    # Training may have saved a torch.compile() wrapper, whose keys have this prefix.
    if state and all(key.startswith("_orig_mod.") for key in state):
        state = {key.removeprefix("_orig_mod."): value for key, value in state.items()}
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve a 4x4 Sudoku with a trained TRM.")
    parser.add_argument("puzzle", help="16 cells, e.g. 0030000031404000; 0 or . means blank")
    parser.add_argument("--config", type=Path, required=True, help="Path to all_config.yaml")
    parser.add_argument("--checkpoint", type=Path, required=True, help="Checkpoint file or directory; defaults to checkpoint_path in config")
    args = parser.parse_args()

    raw_puzzle = parse_puzzle(args.puzzle)
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    data_path = Path(config["data_paths"][0])
    checkpoint_path = args.checkpoint or Path(config["checkpoint_path"])
    checkpoint = latest_checkpoint(checkpoint_path)

    metadata_path = data_path / "train" / "dataset.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata["seq_len"] != 16:
        raise ValueError(f"Dataset metadata says seq_len={metadata['seq_len']}; expected 16.")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    arch = config["arch"]
    model_cfg = {key: value for key, value in arch.items() if key not in {"name", "loss"}}
    model_cfg.update(
        batch_size=1,
        vocab_size=metadata["vocab_size"],
        seq_len=metadata["seq_len"],
        num_puzzle_identifiers=metadata["num_puzzle_identifiers"],
        causal=False,
    )
    loss_cfg = {key: value for key, value in arch["loss"].items() if key != "name"}

    model_cls = load_model_class(arch["name"])
    loss_head_cls = load_model_class(arch["loss"]["name"])
    
    model = model_cls(model_cfg)
    model = loss_head_cls(model, **loss_cfg).to(device)
    
    model.load_state_dict(load_state_dict(checkpoint, device), strict=True)
    model.eval()

    # Ordinary digits are shifted only inside the wrapper: blank 0 -> token 1,
    # digit 1 -> token 2, ..., digit 4 -> token 5. Label 0 is ignored at inference.
    batch = {
        "inputs": torch.tensor([[value + 1 for value in raw_puzzle]], dtype=torch.long, device=device),
        "labels": torch.full(
            (1, 16), metadata.get("ignore_label_id", 0), dtype=torch.long, device=device
        ),
        "puzzle_identifiers": torch.full(
            (1,), metadata.get("blank_identifier_id", 0), dtype=torch.long, device=device
        ),
    }

    with torch.inference_mode():
        with torch.device(device):
            carry = model.initial_carry(batch)

        all_finish = False
        while not all_finish:
            carry, _loss, _metrics, predictions, all_finish = model(
                carry=carry, batch=batch, return_keys=["preds"]
            )

    token_ids = predictions["preds"][0].detach().cpu().tolist()
    # Decode TRM tokens back to ordinary Sudoku values. Token 0 is padding and
    # is shown as ? because it is not a Sudoku cell value.
    decoded = ["?" if token == 0 else str(token - 1) for token in token_ids]

    print(f"\nCheckpoint: {checkpoint}")
    print("Prediction:")
    for row in range(4):
        print(" ".join(decoded[row * 4 : (row + 1) * 4]))
    print("Flat output:", "".join(decoded))
    if "?" in decoded:
        print("Note: ? means the model predicted the padding token, not a Sudoku symbol.")


if __name__ == "__main__":
    main()
