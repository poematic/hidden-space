import os
import json
import csv
import pandas as pd
import numpy as np
import math
import shutil

from typing import Optional
from argdantic import ArgParser
from pydantic import BaseModel
from huggingface_hub import hf_hub_download
from tqdm import tqdm

from common import PuzzleDatasetMetadata

N: int = None
cli = ArgParser()


class DataProcessConfig(BaseModel):
    n: int = 9
    source_repo: Optional[str] = None
    output_dir: Optional[str] = None
    subsample_size: Optional[int] = None
    min_difficulty: Optional[int] = None
    num_aug: int = 0


def shuffle_sudoku(board: np.ndarray, solution: np.ndarray): # Does not check for duplicates
    num_cells = N * N
    num_bands = math.isqrt(N)
    
    # Create a random digit mapping: a permutation of [0, 1, 2, ..., N], with zero (blank) unchanged
    digit_map = np.pad(np.random.permutation(np.arange(1, N + 1)), (1, 0))
    
    # Randomly decide whether to transpose.
    transpose_flag = np.random.rand() < 0.5

    # Generate a valid row permutation:
    # - Shuffle the num_bands bands (each band = num_bands rows) and for each band, shuffle its num_bands rows.
    bands = np.random.permutation(num_bands)
    row_perm = np.concatenate([b * num_bands + np.random.permutation(num_bands) for b in bands])

    # Similarly for columns (stacks).
    stacks = np.random.permutation(num_bands)
    col_perm = np.concatenate([s * num_bands + np.random.permutation(num_bands) for s in stacks])

    # Build an num_cells->num_cells mapping. For each new cell at (i, j)
    # (row index = i // N, col index = i % N),
    # its value comes from old row = row_perm[i//N] and old col = col_perm[i%N].
    mapping = np.array([row_perm[i // N] * N + col_perm[i % N] for i in range(num_cells)])

    def apply_transformation(x: np.ndarray) -> np.ndarray:
        # Apply transpose flag
        if transpose_flag:
            x = x.T
        # Apply the position mapping.
        new_board = x.flatten()[mapping].reshape(N, N).copy()
        # Apply digit mapping
        return digit_map[new_board]

    return apply_transformation(board), apply_transformation(solution)


def convert_subset(set_name: str, config: DataProcessConfig):
    num_cells = N * N
    
    inputs = []
    labels = []
    
    if N == 9: 
        # Read CSV
        with open(hf_hub_download(config.source_repo, f"{set_name}.csv", repo_type="dataset"), newline="") as csvfile:
            shutil.copy(csvfile.name, f"{set_name}_data.csv")
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for _, question, answer, rating in reader:
                if (config.min_difficulty is None) or (int(rating) >= config.min_difficulty):
                    assert len(question) == num_cells and len(answer) == num_cells

                    inputs.append(np.frombuffer(question.replace('.', '0').encode(), dtype=np.uint8).reshape(N, N) - ord('0'))
                    labels.append(np.frombuffer(answer.encode(), dtype=np.uint8).reshape(N, N) - ord('0'))
    else:
        # Read Parquet
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
                    assert len(question) == num_cells and len(answer) == num_cells

                    inputs.append(np.frombuffer(question.replace('.', '0').encode(), dtype=np.uint8).reshape(N, N) - ord('0'))
                    labels.append(np.frombuffer(answer.encode(), dtype=np.uint8).reshape(N, N) - ord('0'))

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
        
        assert np.all((arr >= 0) & (arr <= N))
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
        seq_len=num_cells,
        vocab_size=1 + 1 + N,  # PAD + "0" ... "N"
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
    
    shutil.move(f"{set_name}_data.csv", f"{config.output_dir}/{set_name}/{set_name}_data.csv")
    
    with open(os.path.join(save_dir, "dataset.json"), "w") as f:
        json.dump(metadata.model_dump(), f)
        
    # Save data
    for k, v in results.items():
        np.save(os.path.join(save_dir, f"all__{k}.npy"), v)
        
    # Save IDs mapping (for visualization only)
    with open(os.path.join(config.output_dir, "identifiers.json"), "w") as f:
        json.dump(["<blank>"], f)


@cli.command(singleton=True)
def preprocess_data(config: DataProcessConfig):
    global N
    N = config.n
    
    if N == 9:
        source_repo = "sapientinc/sudoku-extreme"
        output_dir = f"data/sudoku-extreme"
    elif N == 4:
        source_repo = "zeyuzy/puzzle-bench"
        output_dir = f"data/sudoku-4x4"
    else:
        raise ValueError(f"n must be 4 or 9, received: {N}")

    config.source_repo = config.source_repo or source_repo
    config.output_dir = config.output_dir or output_dir

    sample_size = "full" if config.subsample_size is None else config.subsample_size
    min_difficulty = "all" if config.min_difficulty is None else config.min_difficulty
    config.output_dir = f"{config.output_dir}-ss-{sample_size}-diff-{min_difficulty}-augs-{config.num_aug}"

    convert_subset("train", config)
    convert_subset("test", config)


if __name__ == "__main__":
    cli()
