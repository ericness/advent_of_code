from typing import List
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

digit_prompt = """
You are excellent at string manipulation and text processing.
You will be processing a string to extract certain characters.
The string contains alphanumeric characters as well as
numeric digits like 0, 1, etc. Identify the first and last digit characters
in the string. Only identify numeric digit characters. Ignore
any letters that spell out the names of numbers like "one",
"two", etc.

Here are some examples:

Input:
1abc2
Output: 
['1', '2']

Input:
pqr3stu8vwx
Output:
['3', '8']

Input:
a1b2c3d4e5f
Output:
['1', '5']

Input:
treb7uchet
Output:
['7', '7']

Input:
2njsevenszzsfltconesixhsflpbpd
Output:
['2', '2']

Input:
6shgbprkpbksnfourfivemvncvg2eight
Output:
['6', '2']

Input:
dssmtmrkonedbbhdhjbf9hq
Output:
['9', '9']

Here is the string you should process:

Input:
{element}

{format_instructions}
"""

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
model = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0)
digit_template = PromptTemplate(template=digit_prompt, input_variables=["element"], partial_variables={"format_instructions": format_instructions})
digit_chain = digit_template | model | output_parser

def process_input(values: List[str]) -> int:
    chunk_size = 1
    return sum([process_chunk(values[i:i+chunk_size]) for i in range(0, 10, chunk_size)])

def process_chunk(values: List[str]) -> int:
    chain_result = digit_chain.invoke({"element": "\n".join(values)})
    return int("".join(chain_result))

if __name__ == "__main__":
    with open("2023/01/data.txt", "r") as d:
        data = [s.strip() for s in d.readlines()]
    result = process_input(data)
    print(result)
