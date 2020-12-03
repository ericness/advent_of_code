import re
from dataclasses import dataclass
from pathlib import Path
from typing import Set, Tuple, List, Iterator

INPUT_FILE_NAME = "/Users/nesseri/github/advent_of_code/2020/data/02_passwords.txt"
INPUT_REGEX = r"([0-9]+)-([0-9]+) (\w): (\w+)"


@dataclass
class Password:
    min_count: int
    max_count: int
    letter: str
    password: str


def load_data(file: Path) -> Iterator[str]:
    """Load list of input from file"""
    with file.open() as f:
        values = f.read().split("\n")
    return filter(None, values)


def parse_line(line: str) -> Password:
    """Parse input line into a Password class"""
    match = re.search(INPUT_REGEX, line)
    return Password(
        int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)
    )


def does_password_follow_policy(password: Password) -> bool:
    """Check if password follows security policy"""
    return (
        password.min_count
        <= password.password.count(password.letter)
        <= password.max_count
    )


if __name__ == "__main__":
    input_file = Path(INPUT_FILE_NAME)
    input_lines = load_data(input_file)
    passwords = [parse_line(line) for line in input_lines]
    follows_policy = [does_password_follow_policy(password) for password in passwords]
    print(sum(follows_policy))
