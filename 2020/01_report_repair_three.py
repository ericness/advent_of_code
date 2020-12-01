from pathlib import Path
from typing import Tuple, List

INPUT_FILE_NAME = "/Users/nesseri/github/advent_of_code/2020/data/01_report_repair.txt"


def load_data(file: Path) -> List[int]:
    """Load list of ints from file"""
    with file.open() as f:
        values = f.read().split('\n')
    return list(map(int, filter(None, values)))


def find_entries(nums: List[int], target: int) -> Tuple[int, int, int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]
    raise ValueError("Matching numbers not found")


if __name__ == '__main__':
    input_file = Path(INPUT_FILE_NAME)
    numbers = load_data(input_file)
    a, b, c = find_entries(numbers, 2020)
    print(f"{a}, {b}, {c}")
    print(f"Product={a*b*c}")
