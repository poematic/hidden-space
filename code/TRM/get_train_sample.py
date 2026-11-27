"""
Usage:
python get_train_sample.py \
  --data_dir data/<data directory> \
  --split train \
  --num_samples 1
"""

import argparse
import json
from pathlib import Path

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--data_dir", type=Path, required=True)
parser.add_argument("--split", choices=["train", "test"], default="train")
parser.add_argument("--num_samples", type=int, default=1)
args = parser.parse_args()

if args.num_samples < 1:
    parser.error("--num_samples must be at least 1")

split_dir = args.data_dir / args.split
metadata = json.loads((split_dir / "dataset.json").read_text())

print(f"\nseq_len={metadata['seq_len']}, vocab_size={metadata['vocab_size']}")

rng = np.random.default_rng()

for set_name in metadata["sets"]:
    inputs = np.load(split_dir / f"{set_name}__inputs.npy", mmap_mode="r")
    labels = np.load(split_dir / f"{set_name}__labels.npy", mmap_mode="r")

    print(f"\nSet: {set_name} | inputs: {inputs.shape} | labels: {labels.shape}")

    indices = rng.choice(
        len(inputs),
        size=min(args.num_samples, len(inputs)),
        replace=False,
    )

    for i in indices:
        print(f"\nExample {i}")
        print("Input: ", inputs[i].tolist())
        print("Label: ", labels[i].tolist())