from typing import Optional
import os
import json
import numpy as np
import pandas as pd
import shutil

from argdantic import ArgParser
from pydantic import BaseModel
from tqdm import tqdm
from huggingface_hub import hf_hub_download

from common import PuzzleDatasetMetadata


cli = ArgParser()


class DataProcessConfig(BaseModel):
    source_repo: str = "zeyuzy/puzzle-bench"
    output_dir: str = "data/sudoku-4x4"

    subsample_size: Optional[int] = None
    min_difficulty: Optional[int] = None
    num_aug: int = 0


def shuffle_sudoku(board: np.ndarray, solution: np.ndarray): # Does not check for duplicates
    # Create a random digit mapping: a permutation of [0, 1, 2, 3, 4], with zero (blank) unchanged
    digit_map = np.pad(np.random.permutation(np.arange(1, 5)), (1, 0))
    
    # Randomly decide whether to transpose.
    transpose_flag = np.random.rand() < 0.5

    # Generate a valid row permutation:
    # - Shuffle the 2 bands and for each band, shuffle its 2 rows.
    bands = np.random.permutation(2)
    row_perm = np.concatenate([b * 2 + np.random.permutation(2) for b in bands])

    # Similarly for columns (stacks).
    stacks = np.random.permutation(2)
    col_perm = np.concatenate([s * 2 + np.random.permutation(2) for s in stacks])

    # Build an 16->16 mapping. For each new cell at (i, j)
    # (row index = i // 4, col index = i % 4),
    # its value comes from old row = row_perm[i//4] and old col = col_perm[i%4].
    mapping = np.array([row_perm[i // 4] * 4 + col_perm[i % 4] for i in range(16)])

    def apply_transformation(x: np.ndarray) -> np.ndarray:
        # Apply transpose flag
        if transpose_flag:
            x = x.T
        # Apply the position mapping.
        new_board = x.flatten()[mapping].reshape(4, 4).copy()
        # Apply digit mapping
        return digit_map[new_board]

    return apply_transformation(board), apply_transformation(solution)


def convert_subset(set_name: str, config: DataProcessConfig):
    # Read CSV
    inputs = []
    labels = []
    
    path = hf_hub_download(config.source_repo, f"sudoku_4x4/{set_name}-00000-of-00001.parquet", repo_type="dataset")
    
    with open(path, "rb") as parquet_file:
        df = pd.read_parquet(parquet_file)
        df = df[["source", "puzzle", "solution", "empty_count"]]
        df = df.rename(columns={"puzzle": "question", "solution": "answer", "empty_count": "rating"})
        df["rating"] = 0
        df["question"] = df["question"].str.replace("0", ".", regex=False)
        df.to_csv(f"{set_name}_data.csv", index=False)
        
        for _, question, answer, rating in df.itertuples(index=False, name=None):
            if (config.min_difficulty is None) or (rating >= config.min_difficulty):
                assert len(question) == 16 and len(answer) == 16

                inputs.append(np.frombuffer(question.replace('.', '0').encode(), dtype=np.uint8).reshape(4, 4) - ord('0'))
                labels.append(np.frombuffer(answer.encode(), dtype=np.uint8).reshape(4, 4) - ord('0'))

    # If subsample_size is specified for the training set,
    # randomly sample the desired number of examples.
    if set_name == "train" and config.subsample_size is not None:
        total_samples = len(inputs)
        if config.subsample_size < total_samples:
            indices = np.random.choice(total_samples, size=config.subsample_size, replace=False)
            inputs = [inputs[i] for i in indices]
            labels = [labels[i] for i in indices]

    # Generate dataset
    num_augments = config.num_aug if set_name == "train" else 0

    results = {k: [] for k in ["inputs", "labels", "puzzle_identifiers", "puzzle_indices", "group_indices"]}
    puzzle_id = 0
    example_id = 0
    
    results["puzzle_indices"].append(0)
    results["group_indices"].append(0)
    
    for orig_inp, orig_out in zip(tqdm(inputs), labels):
        for aug_idx in range(1 + num_augments):
            # First index is not augmented
            if aug_idx == 0:
                inp, out = orig_inp, orig_out
            else:
                inp, out = shuffle_sudoku(orig_inp, orig_out)

            # Push puzzle (only single example)
            results["inputs"].append(inp)
            results["labels"].append(out)
            example_id += 1
            puzzle_id += 1
            
            results["puzzle_indices"].append(example_id)
            results["puzzle_identifiers"].append(0)
            
        # Push group
        results["group_indices"].append(puzzle_id)
        
    # To Numpy
    def _seq_to_numpy(seq):
        arr = np.concatenate(seq).reshape(len(seq), -1)
        
        assert np.all((arr >= 0) & (arr <= 4))
        return arr + 1
    
    results = {
        "inputs": _seq_to_numpy(results["inputs"]),
        "labels": _seq_to_numpy(results["labels"]),
        
        "group_indices": np.array(results["group_indices"], dtype=np.int32),
        "puzzle_indices": np.array(results["puzzle_indices"], dtype=np.int32),
        "puzzle_identifiers": np.array(results["puzzle_identifiers"], dtype=np.int32),
    }

    # Metadata
    metadata = PuzzleDatasetMetadata(
        seq_len=16,
        vocab_size=5 + 1,  # PAD + "0" ... "4"
        pad_id=0,
        ignore_label_id=0,
        blank_identifier_id=0,
        num_puzzle_identifiers=1,
        total_groups=len(results["group_indices"]) - 1,
        mean_puzzle_examples=1,
        total_puzzles=len(results["puzzle_indices"]) - 1, 
        sets=["all"]
    )

    # Save metadata as JSON.
    save_dir = os.path.join(config.output_dir, set_name)
    os.makedirs(save_dir, exist_ok=True)
    
    with open(os.path.join(save_dir, "dataset.json"), "w") as f:
        json.dump(metadata.model_dump(), f)
        
    # Save data
    for k, v in results.items():
        np.save(os.path.join(save_dir, f"all__{k}.npy"), v)
        
    # Save IDs mapping (for visualization only)
    with open(os.path.join(config.output_dir, "identifiers.json"), "w") as f:
        json.dump(["<blank>"], f)
    
    shutil.move(f"{set_name}_data.csv", f"{config.output_dir}/{set_name}/{set_name}_data.csv")


@cli.command(singleton=True)
def preprocess_data(config: DataProcessConfig):
    convert_subset("train", config)
    convert_subset("test", config)


if __name__ == "__main__":
    cli()
