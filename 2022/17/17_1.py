import numpy as np
import itertools
def main():
    shapes = [
        np.array([[0,0], [1,0], [2,0], [3,0]]),
        np.array([[1,0], [0,1], [1,1], [2,1], [1,2]]),
        np.array([[0,0], [1,0], [2,0], [2,1], [2,2]]),
        np.array([[0,0], [0,1], [0,2], [0,3]]),
        np.array([[0,0], [0,1], [1,0], [1,1]])
        ]
    
    jets = []
    with open("17/input") as f:
        line = f.readline()
        for c in line.rstrip():
            jets.append(c)

    chamber = np.full((9, (3 * 2022) + 1), False)
    chamber[:, 0] = True
    chamber[0, :] = True
    chamber[-1, :] = True

    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(formatter={"bool":lambda x: "#" if x else "."})
    top = 0
    shape_iter = itertools.cycle(shapes)
    jet_iter = itertools.cycle(jets)
    for _ in range(2022):
        spawn = np.array([3, top + 4])
        shape = next(shape_iter)
        rock = spawn + shape
        while True:
            jet = next(jet_iter)
            direction = [1,0] if jet == ">" else [-1,0]
            next_pos = rock + direction
            if not any([chamber[tuple(point)] for point in next_pos]):
                rock = next_pos
            direction = [0, -1]
            next_pos = rock + direction
            if any([chamber[tuple(point)] for point in next_pos]):
                break
            rock = next_pos
        for point in rock:
            chamber[tuple(point)] = True
            top = max(top, point[1])
    
    print(top)

if __name__ == "__main__":
    main()