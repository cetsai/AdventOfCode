"""
Part 2 is the same problem, but the inputs are much bigger.

Instead of separate races, we need to ignore whitespace and read the input as
a single race.

Due to the approach taken in part 1, the solution is practically unchanged.
"""
import re
import math
from functools import reduce


def main():
    races = []
    with open("input") as f:
        time = int(reduce(lambda x, y: x + y, re.findall(r"\d+", f.readline())))
        record = int(reduce(lambda x, y: x + y, re.findall(r"\d+", f.readline())))

        sqrt_d = math.sqrt((time ** 2) - (4 * record))
        min_dist = (time - sqrt_d) / 2
        max_dist = (time + sqrt_d) / 2
        num_ways = int(math.ceil(max_dist) - math.floor(min_dist)) - 1
        print(num_ways)


if __name__ == "__main__":
    main()
