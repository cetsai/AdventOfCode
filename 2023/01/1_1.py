"""
https://adventofcode.com/2023/day/1

Each line in the input has at least one digit. We need to form a two 
digit number by combining the first and last appearance of a digit.
Final answer is the sum of these two digit numbers for all lines.

My solution is to use a regular expression search to find all digits in
a line, then simply take the first and last to add to the result.
"""
import re


def main():
    result = 0
    with open("input") as f:
        for line in f:
            digits = list(map(int, re.findall(r"\d", line)))
            result += (digits[0] * 10) + digits[-1]
    print(result)


if __name__ == "__main__":
    main()