from pathlib import Path
from typing import Set, Tuple

INPUT_FILE_NAME = "/Users/nesseri/github/advent_of_code/2020/data/01_report_repair.txt"


def load_data(file: Path) -> Set:
    """Load list of ints from file"""
    with file.open() as f:
        values = f.read().split('\n')
    return set(map(int, filter(None, values)))


def find_2020_entries(nums: Set) -> Tuple[int, int]:
    for num in nums:
        if 2020 - num in nums:
            return num, 2020 - num
    raise ValueError("Matching numbers not found")


if __name__ == '__main__':
    input_file = Path(INPUT_FILE_NAME)
    numbers = load_data(input_file)
    a, b = find_2020_entries(numbers)
    print(f"Product={a*b}")
