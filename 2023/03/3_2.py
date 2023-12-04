"""
For this part we need to find a more specific case.

Gears are represented as any '*' symbol with two adjacent part numbers.
A gear's "gear ratio" is equal to the product of these part numbers.

For the solution, we can use the same approach as part 1, but in the 
second pass look for '*' symbols and find the set of adjacent part ids.
If the size of this set is 2, then compute the gear ratio and add it to
the result.
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
    
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            adjacent_parts_ids = set()
            char = grid[row][col]
            if not char == '*':
                continue
            for dx, dy in it.product([-1, 0, 1], repeat=2):
                x = row + dx
                y = col + dy
                if x not in range(len(grid)) or y not in range(len(grid[row])):
                    continue
                if grid[x][y].isdigit():
                    adjacent_parts_ids.add(int(grid[x][y]))
            if len(adjacent_parts_ids) == 2:
                gear_ratio = 1
                for part in adjacent_parts_ids:
                    gear_ratio *= part_numbers[part]
                result += gear_ratio
    print(result)


if __name__ == "__main__":
    main()