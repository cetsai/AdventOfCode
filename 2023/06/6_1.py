"""
https://adventofcode.com/2023/day/6

The input is a list of distances and times which describe a series of races.
To win a race, you need to go further than the listed distance within the
listed time. During the race you can spend some amount of time charging,
during which you are stationary, and the rest of the time is spent moving at
a speed equal to the amount of time spent charging. For each race, there is
a number of integer charge times that allow you to win. The task is to find
the product of these numbers for all races.

The formula for distance travelled(D) based on charge time(Tc) and
race time(Tr) is D = -Tc^2 + TrTc. This is simply an inverted parabola.
Using this fact, we can find the range of charge times that will get beat the
record(R) by shifting the parabola down by R and finding the x-intercepts
using the quadratic formula.

D = -(Tc)^2 + Tr(Tc) -　R
a = -1, b = race time, c = -record
quadratic formula: (-b +- sqrt(b^2 - 4ac)) / 2a
substituting => (Tr + sqrt(Tr^2 - 4R)) / 2 and (Tr - sqrt(Tr^2 - 4R)) / 2
"""
import re
import math


def main():
    races = []
    with open("input") as f:
        times = list(map(int, re.findall(r"\d+", f.readline())))
        distances = list(map(int, re.findall(r"\d+", f.readline())))
        races = zip(times, distances)

    result = 1
    for time, record in races:
        sqrt_d = math.sqrt((time ** 2) - (4 * record))
        min_dist = (time - sqrt_d) / 2
        max_dist = (time + sqrt_d) / 2
        num_ways = int(math.ceil(max_dist) - math.floor(min_dist)) - 1
        result *= num_ways
    print(result)


if __name__ == "__main__":
    main()
