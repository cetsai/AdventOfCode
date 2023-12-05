"""
https://adventofcode.com/2023/day/4

Each line of the input is a scratch card, with a set of winning numbers
on the left of the '|' and a set of candidate numbers to the right. The
card is scored based on matches between candidate numbers and winning
numbers. The score starts at 1 for the first match and doubles for each
subsequent match. The task is to find the sum of all the scores.

The solution is very straightforward-- read each line of the input,
computing the score by using set intersection, and add the score to the
result.
"""
import re


def main():
    result = 0
    with open("input") as f:
        for line in f:
            colon_index = line.find(':')
            bar_index = line.find('|')
            winning_numbers = re.findall(r"\d+", line[colon_index:bar_index])
            candidate_numbers = re.findall(r"\d+", line[bar_index:])
            scoring_numbers = set(winning_numbers) & set(candidate_numbers)
            if len(scoring_numbers) > 0:
                result += 2 ** (len(scoring_numbers) - 1)
    print(result)


if __name__ == "__main__":
    main()