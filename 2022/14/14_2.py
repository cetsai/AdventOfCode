import numpy as np
import itertools

def find_resting_pos(grid, start):
    sand = start
    while True:
        next_steps = np.array([[0, 1], [-1, 1], [1, 1]])
        next_steps += sand
        for step in next_steps:
            if np.any((step < 0) | (step >= grid.shape)):
                print(step)
                return None
            if not grid[tuple(step)]:
                sand = step
                break
        else:
            return sand

def main():
    paths = []
    x_min = x_max = 500
    y_max = 0
    with open("input") as f:
        for line in map(str.rstrip, f):
            path = []
            for coord in line.split("->"):
                x, y = map(int, coord.split(","))
                x_min, x_max = (min(x, x_min), max(x, x_max))
                y_max = max(y, y_max)
                path.append(tuple(map(int, coord.split(","))))
            paths.append(path)
    
    y_max += 3
    paths = [list(map(lambda coord: (coord[0] - 500 + y_max, coord[1]), path)) for path in paths]
    grid = np.full(((2 * y_max) + 1, y_max), False)
    grid[:, -1] = True
    
    for path in paths:
        # itertools.pairwise in 3.10+
        a, b = itertools.tee(path)
        next(b, None)
        for start, end in zip(a, b):
            x1, y1 = min(start[0], end[0]), min(start[1], end[1]) 
            x2, y2 = max(start[0], end[0]), max(start[1], end[1])
            grid[x1:(x2+1), y1:(y2+1)] = True
        
    spawn = np.array([y_max, 0])
    count = 0
    while True:
        resting_pos = find_resting_pos(grid, spawn)
        if resting_pos is None:
            assert False
        else:
            grid[tuple(resting_pos)] = True
            count += 1
            if np.all(resting_pos == spawn):
                break

    print(count)

if __name__ == "__main__":
    main()