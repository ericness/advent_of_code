from typing import List
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

digit_prompt = """
There is a group of strings in triple backticks below.
Each string is separated by a newline character.
The strings contain alphanumeric characters as well as
digits. Identify the first and last digit characters
in each string. Only identify numeric digit characters.
Output a group of strings of the same
length with the two digits appended to each other.

Here is an example group of strings:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
2njsevenszzsfltconesixhsflpbpd
6shgbprkpbksnfourfivemvncvg2eight
dssmtmrkonedbbhdhjbf9hq
```
What you should output is between triple backticks:
```
12
38
15
77
22
62
99
```

Here is the list of strings you should process:
```
{elements}
```

"""

# output_parser = CommaSeparatedListOutputParser()
# format_instructions = output_parser.get_format_instructions()
model = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0)
digit_template = PromptTemplate(template=digit_prompt, input_variables=["elements"]) #, partial_variables={"format_instructions": format_instructions})
digit_chain = digit_template | model # | output_parser

def process_input(values: List[str]) -> int:
    chunk_size = 10
    return sum([process_chunk(values[i:i+chunk_size]) for i in range(0, 1, chunk_size)])

def process_chunk(values: List[str]) -> int:
    chain_result = digit_chain.invoke({"elements": "\n".join(values)})
    return sum(chain_result)

if __name__ == "__main__":
    with open("2023/01/data.txt", "r") as d:
        data = [s.strip() for s in d.readlines()]
    result = process_input(data)
    print(result)
