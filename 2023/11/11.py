"""
https://adventofcode.com/2023/day/11

The input is a grid of characters, where '.' represents empty space and '#'
represents a galaxy. Additionally, each empty row or column is expanded as if
it were two empty rows/columns. The task is to find the manhattan distance
between each pair of galaxies including this expansion. The final answer is the
sum of these distances.

My idea is to use an array that keeps track of the number of empty rows at each
column and vice versa, and when computing the distance between two galaxies, use
these arrays to find the amount of expansion and add it to the manhattan
distance.

For part 2, instead of expanding an empty line into 2, we need to expand it
into 1,000,000 instead. Since this only changes a single variable, I kept the
solutions for both days in a single file.
"""
import itertools as it

def main():
    empty_rows: set[int] = set()
    empty_cols: set[int]
    num_rows = 0
    num_cols = 0
    galaxies = []
    with open("input") as f:
        empty_cols = set(range(len(f.readline().rstrip())))
        num_cols = len(empty_cols)
        f.seek(0)
        for row, line in enumerate(f):
            galaxy_cols = set()
            for col, char in enumerate(line):
                if char == '#':
                    galaxy_cols.add(col)
                    galaxies.append((row, col))
            if not galaxy_cols:
                empty_rows.add(row)
            else:
                empty_cols = empty_cols - galaxy_cols
            num_rows += 1

    # expansion amount = 1      # part 1
    expansion_amount = 999999   # part 2
    row_expansion = list(it.accumulate([expansion_amount if i in empty_rows else 0 for i in range(num_rows)]))
    col_expansion = list(it.accumulate([expansion_amount if i in empty_cols else 0 for i in range(num_cols)]))
    total = 0
    for (x1, y1), (x2, y2) in it.combinations(galaxies, 2):
        manhattan_distance = abs(x2 - x1) + abs(y2 - y1)
        expansion = abs(row_expansion[x2] - row_expansion[x1]) + abs(col_expansion[y2] - col_expansion[y1])
        total += manhattan_distance + expansion
    print(total)


if __name__ == "__main__":
    main()
