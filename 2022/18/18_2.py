import numpy as np

def main():
    neighbor_offsets = [
        np.array([1, 0, 0]),
        np.array([-1, 0, 0]),
        np.array([0, 1, 0]),
        np.array([0, -1, 0]),
        np.array([0, 0, 1]),
        np.array([0, 0, -1])
    ]

    grid = np.full((25, 25, 25), False)
    total = 0
    with open("18/input") as f:
        for line in f:
            coord = np.array(list(map(int, line.rstrip().split(","))))
            grid[tuple(coord)] = True
            neighbors = coord + neighbor_offsets
            total += 6 - (2 * sum([grid[tuple(n)] for n in neighbors]))
    print(total)

if __name__ == "__main__":
    main()