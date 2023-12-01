"""
https://adventofcode.com/2023/day/1

Each line in the input has at least one digit. We need to form a two 
digit number by combining the first and last appearance of a digit.
Final answer is the sum of these two digit numbers for all lines.
"""
import re


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            digits = list(map(int, re.findall(r"\d", line)))
            sum += (digits[0] * 10) + digits[-1]
    print(sum)


if __name__ == "__main__":
    main()