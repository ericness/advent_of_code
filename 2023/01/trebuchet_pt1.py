from langchain.output_parsers import CommaSeparatedListOutputParser

digit_prompt = """
There is a list of strings in triple backticks below.
The strings contain alphanumeric characters as well as
digits. Identify the first and last digit characters
in each string. Output a list of the same length with
the two digits appended to each other.

Here is an example list:
```
["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
```
What you should output is between triple backticks:
```
["12", "38", "15", "77"]
```

Here is the list of strings you should process:
```
{elements}
```
"""

def process_input(values: List[str]) -> int:
    chunk_size = 10
    return sum(process_chunk([values[i:i+chunk_size]) for i in range(0, len(values), chunk_size)])

def process_chunk(values: List[str]) -> int:

model = ChatOpenAI(model="gpt-3.5-turbo")

if __name__ == "__main__":
    with open("data.txt", "r") as d:
        data = [s.strip() for s in d.readlines()]
    process_input(data)