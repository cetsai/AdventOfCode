"""
https://adventofcode.com/2023/day/9

Each line of the input is a sequence of numbers. The task is to predict
the next number in each sequence. This can be achieved by taking the
difference between consecutive entries to obtain a new sequence and
repeating this process until the sequence is all zeroes. Then, add a
zero to this sequence and use that to find the next element in the
previous sequence in this process. Continue until you get back to the
original sequence. The final answer is the sum of these precdictions.

Pretty simple solution by using recursion in the predict_sequence
function. I got the all_equal definition from python's documentation:
https://docs.python.org/3/library/itertools.html#itertools-recipes
"""
from itertools import groupby, pairwise
from functools import reduce


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def predict_sequence(sequence: list[int]) -> int:
    if all_equal(sequence):
        return sequence[0]
    differences = []
    for first, second in pairwise(sequence):
        differences.append(second - first)
    return sequence[-1] + predict_sequence(differences)


def main():
    sequences = []
    with open("input") as f:
        for line in f:
            sequences.append(list(map(int, line.split(" "))))

    result = reduce(lambda x, y: x + y, map(predict_sequence, sequences))
    print(result)


if __name__ == "__main__":
    main()
