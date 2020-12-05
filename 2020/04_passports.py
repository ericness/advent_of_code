from pathlib import Path
import re
from typing import Dict, Iterator, Tuple


INPUT_REGEX = r"([a-z0-9#]+):([a-z0-9#]+)"
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
YEAR_REGEX = r"^\d{4}$"
HEIGHT_REGEX = r"^(\d+)(in|cm)$"
HAIR_COLOR_REGEX = r"^#[0-9a-f]{6}$"
EYE_COLOR_REGEX = r"^amb|blu|brn|gry|grn|hzl|oth$"
PASSPORT_ID_REGEX = r"^[0-9]{9}$"


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


def has_required_fields(passport: Dict[str, str]) -> bool:
    """Check if passport is valid"""
    return len(REQUIRED_FIELDS.intersection(set(passport.keys()))) == len(
        REQUIRED_FIELDS
    )


def is_birth_year_valid(passport: Dict[str, str]) -> bool:
    """Check if birth year field is valid"""
    birth_year = passport["byr"]
    return re.match(YEAR_REGEX, birth_year) and 1920 <= int(birth_year) <= 2002


def is_issue_year_valid(passport: Dict[str, str]) -> bool:
    """Check if issue year field is valid"""
    issue_year = passport["iyr"]
    return re.match(YEAR_REGEX, issue_year) and 2010 <= int(issue_year) <= 2020


def is_expiration_year_valid(passport: Dict[str, str]) -> bool:
    """Check if expiration year field is valid"""
    expiration_year = passport["eyr"]
    return (
        re.match(YEAR_REGEX, expiration_year) and 2020 <= int(expiration_year) <= 2030
    )


def is_height_valid(passport: Dict[str, str]) -> bool:
    """Check if height is valid"""
    match = re.match(HEIGHT_REGEX, passport["hgt"])
    if not match:
        return False
    height, unit = match.groups()
    return (150 <= int(height) <= 193 and unit == "cm") or (
        59 <= int(height) <= 76 and unit == "in"
    )


def is_hair_color_valid(passport: Dict[str, str]) -> bool:
    """Check if hair color field is valid"""
    hair_color = passport["hcl"]
    return True if re.match(HAIR_COLOR_REGEX, hair_color) else False


def is_eye_color_valid(passport: Dict[str, str]) -> bool:
    """Check if eye color field is valid"""
    eye_color = passport["ecl"]
    return True if re.match(EYE_COLOR_REGEX, eye_color) else False


def is_passport_id_valid(passport: Dict[str, str]) -> bool:
    """Check if issue year field is valid"""
    passport_id = passport["pid"]
    return True if re.match(PASSPORT_ID_REGEX, passport_id) else False


if __name__ == "__main__":
    validators = [
        is_birth_year_valid,
        is_issue_year_valid,
        is_expiration_year_valid,
        is_height_valid,
        is_hair_color_valid,
        is_eye_color_valid,
        is_passport_id_valid,
    ]
    current_dir = Path(__file__).parent.absolute()
    input_file = current_dir / "data" / "04_passports.txt"
    input_lines = load_data(input_file)
    passports = [parse_line(line) for line in input_lines]
    passports_with_required_fields = [
        passport for passport in passports if has_required_fields(passport)
    ]
    valid = [
        all([validator(passport) for validator in validators])
        for passport in passports_with_required_fields
    ]
    print(sum(valid))
