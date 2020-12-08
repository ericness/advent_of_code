from pathlib import Path
import re
from typing import Iterator, Set

QUESTION_REGEX = r"([a-z])"


def load_data(file: Path) -> Iterator[str]:
    """Load list of input from file"""
    with file.open() as f:
        values = f.read().split("\n\n")
    return values


def process_group(questions: str) -> Set[str]:
    """Get set of unique question ids"""
    return set(re.findall(QUESTION_REGEX, questions))


def process_group_all(questions: str) -> Set[str]:
    """Set set of question ids for all passengers"""
    passengers = questions.split("\n")
    passengers_sets = [
        set(re.findall(QUESTION_REGEX, passenger)) for passenger in passengers
    ]
    return set.intersection(*passengers_sets)


if __name__ == "__main__":
    current_dir = Path(__file__).parent.absolute()
    input_file = current_dir / "data" / "06_custom_customs.txt"
    input_lines = load_data(input_file)
    question_sets = [process_group(line) for line in input_lines]
    print(sum([len(question_set) for question_set in question_sets]))
    question_all_sets = [process_group_all(line) for line in input_lines]
    print(sum([len(question_set) for question_set in question_all_sets]))
