from pathlib import Path
from typing import Iterator

import numpy as np


INPUT_FILE_NAME = "/Users/nesseri/github/advent_of_code/2020/data/03_trees.txt"
INPUT_MAP = {".": 0, "#": 1}


def load_data(file: Path) -> Iterator[str]:
    """Load list of input from file"""
    with file.open() as f:
        values = f.read().split("\n")
    return filter(None, values)


def process_line(line: str) -> np.array:
    """Convert string representation into array"""
    return np.array([INPUT_MAP[c] for c in line])


def calculate_tree_count(
    terrain_array: np.array, right_move: int, down_move: int
) -> int:
    """Calculate how many trees get hit"""
    trees = 0
    row = 0
    column = 0

    while row + down_move < terrain_array.shape[0]:
        row += down_move
        column = (column + right_move) % terrain_array.shape[1]
        trees += terrain_array[row, column]

    return trees


if __name__ == "__main__":
    input_file = Path(INPUT_FILE_NAME)
    input_lines = load_data(input_file)
    arrays = [process_line(line) for line in input_lines]
    terrain = np.vstack(arrays)
    tree_count_1_1 = calculate_tree_count(terrain, 1, 1)
    tree_count_3_1 = calculate_tree_count(terrain, 3, 1)
    tree_count_5_1 = calculate_tree_count(terrain, 5, 1)
    tree_count_7_1 = calculate_tree_count(terrain, 7, 1)
    tree_count_1_2 = calculate_tree_count(terrain, 1, 2)
    print(
        tree_count_1_1
        * tree_count_3_1
        * tree_count_5_1
        * tree_count_7_1
        * tree_count_1_2
    )
