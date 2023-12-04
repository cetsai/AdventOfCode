"""
https://adventofcode.com/2023/day/3

The input is a grid of characters. These digits can be periods, which
are filler characters; digits, which are part of a part number; or
symbols, which are any other character. The task is to find all part
numbers which are adjacent (diagonally included) to a symbol. A part
number is any consecutive string of digits in a line.

My solution does this in two passes. First, the input is read into a
2D array. Second, we loop over the array and if we encounter a symbol,
we add all adjacent parts to a set. To handle duplicate part numbers,
contiguous digits are assigned an id when they are read and this id is
substituted into the grid. Later, when computing the result, the ids are
converted back to the original part numbers.
"""
import re
import itertools as it


def main():
    grid = []
    part_numbers = []
    with open("input") as f: 
        next_part_id = 0
        for line in f:
            row = []
            part_strings = re.findall(r"\d+", line)
            part_index = 0
            reading_part = False
            for char in line.rstrip():
                if char.isdigit():
                    reading_part = True
                    row.append(str(next_part_id))
                else:
                    if reading_part:
                        reading_part = False
                        part_numbers.append(int(part_strings[part_index]))
                        next_part_id += 1
                        part_index += 1
                    row.append(char)
            if reading_part:
                part_numbers.append(int(part_strings[part_index]))
                next_part_id += 1
            grid.append(row)

    adjacent_parts_ids = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char == '.' or char.isdigit():
                continue
            for dx, dy in it.product([-1, 0, 1], repeat=2):
                x = row + dx
                y = col + dy
                if x not in range(len(grid)) or y not in range(len(grid[row])):
                    continue
                if grid[x][y].isdigit():
                    adjacent_parts_ids.add(int(grid[x][y]))
    print(sum([part_numbers[i] for i in adjacent_parts_ids]))


if __name__ == "__main__":
    main()