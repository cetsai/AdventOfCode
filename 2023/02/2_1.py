"""
https://adventofcode.com/2023/day/2

Each line of the input describes one game, in which colored cubes are 
drawn out of a bag. The task is to find which games are possible with a 
bag containing 12 red, 13 green, and 14 blue cubes. The final answer is
the sum of the game numbers of these 'possible' games.

This is a simple exercise in parsing the input string and comparing the
numbers drawn for each color with the total of that color in the bag. 
The input separates the draws into sets, where each set can have up to
one draw for each color, but this has no impact on the result, so we can
treat draws as independent.
"""
import re


def main():
    bag = {
        "red": 12,
        "green": 13,
        "blue":14,
    }
    game_pattern = re.compile(r"Game (\d+): ")
    draw_pattern = re.compile(r"(?:(?P<num>\d+) "
                              r"(?P<color>(?:red)|(?:blue)|(?:green)))+")
    result = 0

    with open("input") as f:
        for line in f:
            game = int(game_pattern.match(line)[1])
            draws = draw_pattern.findall(line)
            for num, color in draws:
                if int(num) > bag[color]:
                    break
            else:
                result += game
    print(result)


if __name__ == "__main__":
    main()