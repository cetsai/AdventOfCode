
# due to how the grid is read, first index is row, second is column
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def neighbors(symbol, pos):
    def translation(offset): return offset[0] + pos[0], offset[1] + pos[1]
    offsets = []
    match symbol:
        case '|':
            offsets = [UP, DOWN]
        case '-':
            offsets = [LEFT, RIGHT]
        case 'L':
            offsets = [UP, RIGHT]
        case 'J':
            offsets = [UP, LEFT]
        case '7':
            offsets = [LEFT, DOWN]
        case 'F':
            offsets = [RIGHT, DOWN]
        case 'S':
            offsets = [UP, RIGHT, LEFT, DOWN]
        case _:
            offsets = []
    return map(translation, offsets)


def main():
    grid = []
    with open("testinput") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(char)
            grid.append(row)

    start = (0, 0)
    for row_index, row in enumerate(grid):
        if 'S' in row:
            start = (row_index, row.index('S'))
            break

    print(start)
    print(grid)
    loop = [start]
    horizon = []
    visited = {start: 0}
    def symbol(pos): return grid[pos[0]][pos[1]]
    for neighbor in neighbors(symbol(start), start):
        if start in neighbors(symbol(neighbor), neighbor):
            horizon.append(neighbor)
    print(horizon)

    while horizon:
        curr = horizon.pop()


if __name__ == "__main__":
    main()
