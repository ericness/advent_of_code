from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List

INPUT_MAP = {"F": "0", "B": "1", "R": "1", "L": "0"}


@dataclass
class Seat:
    """Plane seat"""

    row: int
    seat: int


def load_data(file: Path) -> Iterator[str]:
    """Load list of input from file"""
    with file.open() as f:
        values = f.read().split("\n")
    return values


def process_line(line: str) -> Seat:
    """Convert string representation into Seat"""
    row = int("".join([INPUT_MAP[c] for c in line[:7]]), 2)
    seat = int("".join([INPUT_MAP[c] for c in line[7:]]), 2)
    return Seat(row=row, seat=seat)


def calculate_seat_id(seat: Seat) -> int:
    """Calculate seat ID"""
    return seat.row * 8 + seat.seat


def find_seat_id(seats: List[int]) -> int:
    """Find the missing seat id with existing seats on both sides"""
    min_seat = min(seats)
    max_seat = max(seats)
    seats_set = set(seats)
    for seat_id in range(min_seat, max_seat):
        if seat_id not in seats_set:
            return seat_id
    return 0


if __name__ == "__main__":
    current_dir = Path(__file__).parent.absolute()
    input_file = current_dir / "data" / "05_binary_boarding.txt"
    input_lines = load_data(input_file)
    seats = [process_line(line) for line in input_lines]
    seat_ids = [calculate_seat_id(seat) for seat in seats]
    print(max(seat_ids))
    print(find_seat_id(seat_ids))
