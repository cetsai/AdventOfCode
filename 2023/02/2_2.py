"""
Find powers of minimal sets

This time instead of seeing if the game is possible, we need to find the
minimal set of cubes in the bag needed to make each game possible. For
each game, we then multiply the numbers of cubes of each color in this
mimimal set to get the 'power' of the set. The final answer is the sum
of the powers of all games.

The solution is similar to part one, except instead of comparing to a
set value, we keep track of the minimal set for each game. As each draw
is read, we check against this minimal set and update if needed. After
each line, we find the power and add it to the result.
"""
import re
from functools import reduce


def main():
    draw_pattern = re.compile(r"(?:(?P<num>\d+) "
                              r"(?P<color>(?:red)|(?:blue)|(?:green)))+")
    result = 0

    with open("input") as f:
        for line in f:
            bag = {"red": 0, "green": 0, "blue": 0}
            draws = draw_pattern.findall(line)
            for num_str, color in draws:
                num = int(num_str)
                if int(num) > bag[color]:
                    bag[color] = num
            result += reduce(lambda x, y: x * y, bag.values())
    print(result)


if __name__ == "__main__":
    main()