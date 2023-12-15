import operator


def main():
    grid = list()
    with open("input") as f:
        for line in map(str.rstrip, f):
            grid.append(list(line))

    total_load = 0
    for i in range(len(grid[0])):
        col = list(map(operator.itemgetter(i), grid))
        num_rocks = 0
        start_load = len(col)
        for row, char in enumerate(col, start=1):
            match char:
                case 'O':
                    num_rocks += 1
                case '#':
                    total_load += int(num_rocks * (start_load + (start_load - num_rocks + 1)) / 2)
                    num_rocks = 0
                    start_load = len(col) - row
                case _:
                    continue
        total_load += int(num_rocks * (start_load + (start_load - num_rocks + 1)) / 2)
    print(total_load)


if __name__ == "__main__":
    main()
