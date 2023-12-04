"""
Same as part 1, except digits can be spelled out e.g. "one" = "1"

My solution uses the same method as part 1, but I preprocess each line
by replacing spelled out digits with their corresponding numerical 
character.

I also sandwich this with the first and last character of each spelled 
out string (e.g. 'seven' = 's7n'), to handle cases where the a letter in
the input is both the first and last letter of a spelled out digit.
"""
import re


def main():
    digit_map = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    result = 0

    with open("input") as f:
        for line in f:
            for old, new in digit_map.items():
               line = line.replace(old, new)
            digits = list(map(int, re.findall(r"\d", line)))
            result += (digits[0] * 10) + digits[-1]
    print(result)


if __name__ == "__main__":
    main()