import re
import numpy as np

def main():
    with open("9/input") as f:
        direction_map = {
            "U": [0, 1],
            "D": [0, -1],
            "L": [-1, 0],
            "R": [1, 0]
        }
        command = re.compile(r"(?P<direction>[UDRL]) (?P<steps>\d+)$")

        rope = np.ones((10, 2))
        visited = set()

        for line in f:
            direction, steps = command.match(line).group("direction", "steps")
            steps = int(steps)
            direction = np.array(direction_map[direction])
            for _ in range(steps):
                rope[0] += direction
                for i in range(1, len(rope)):
                    diff = rope[i-1] - rope[i]
                    if np.linalg.norm(diff) == 2:
                        rope[i] += diff / np.linalg.norm(diff)
                    elif np.linalg.norm(diff) > 2:
                        rope[i] += diff / abs(diff)
                visited.add(tuple(rope[-1]))
            
        print(len(visited))


if __name__ == "__main__":
    main()