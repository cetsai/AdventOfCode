import numpy as np
from collections import deque

def main():
    input_map = []
    start = None
    end = None
    with open("input") as f:
        for x, line in enumerate(f):
            row = []
            for y, c in enumerate(line.rstrip()):
                if c == "S":
                    start = (x, y)
                    row.append(ord('a') - ord('a'))
                elif c == "E":
                    end = (x, y)
                    row.append(ord('z') - ord('a'))
                else:
                    row.append(ord(c) - ord('a'))
            input_map.append(row)
    
    elevation_map = np.array(input_map)
    distance_map = np.full(elevation_map.shape, -1)
    neighbor_offsets = np.array([[-1, 0], [1,0], [0,-1], [0,1]])
    
    horizon = deque()
    horizon.append(start)
    distance_map[start] = 0
    while True:
        location = horizon.popleft()
        if np.all(location == end):
            break

        neighbors = np.array(location) + neighbor_offsets
        for neighbor in neighbors:
            if np.any(neighbor < 0) or np.any(neighbor >= np.array(distance_map.shape)):
                continue
            if distance_map[tuple(neighbor)] > 0:
                continue
            if elevation_map[tuple(neighbor)] <= elevation_map[location] + 1:
                horizon.append(tuple(neighbor))
                distance_map[tuple(neighbor)] = distance_map[location] + 1
        
        if not horizon:
            break

    print(distance_map[end])

if __name__ == "__main__":
    main()