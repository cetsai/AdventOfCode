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

        head = np.zeros(2)
        tail = np.zeros(2)
        visited = set()

        for line in f:
            direction, steps = command.match(line).group("direction", "steps")
            steps = int(steps)
            direction = np.array(direction_map[direction])
            for _ in range(steps):
                head += direction
                diff = head - tail
                if np.linalg.norm(diff) == 2:
                    tail += diff / np.linalg.norm(diff)
                elif np.linalg.norm(diff) > 2:
                    tail += diff / abs(diff)
                visited.add(tuple(tail))
            
        print(len(visited))


if __name__ == "__main__":
    main()