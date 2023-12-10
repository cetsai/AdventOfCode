"""
For part 2, we need to predict the previous value in each of the
original sequences using the same method.

Pretty much a copy-paste of part 1; just needed to change the end of the
list that predict_sequence operates on.
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
    return sequence[0] - predict_sequence(differences)


def main():
    sequences = []
    with open("input") as f:
        for line in f:
            sequences.append(list(map(int, line.split(" "))))

    result = reduce(lambda x, y: x + y, map(predict_sequence, sequences))
    print(result)


if __name__ == "__main__":
    main()
