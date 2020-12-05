from pathlib import Path
import re
from typing import Dict, Iterator, Tuple


INPUT_REGEX = "([a-z0-9#]+):([a-z0-9#]+)"
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def load_data(file: Path) -> Iterator[str]:
    """Load list of input from file"""
    with file.open() as f:
        values = f.read().split("\n\n")
    return values


def parse_line(line: str) -> Dict[str, str]:
    """Parse input line into a Password class"""
    entries = re.findall(INPUT_REGEX, line)
    passport = {field: value for field, value in entries}
    return passport


def is_passport_valid(passport: Dict[str, str]):
    """Check if passport is valid"""
    return len(REQUIRED_FIELDS.intersection(set(passport.keys()))) == len(
        REQUIRED_FIELDS
    )


if __name__ == "__main__":
    current_dir = Path(__file__).parent.absolute()
    input_file = current_dir / "data" / "04_passports.txt"
    input_lines = load_data(input_file)
    passports = [parse_line(line) for line in input_lines]
    valid = [is_passport_valid(passport) for passport in passports]
    print(sum(valid))
