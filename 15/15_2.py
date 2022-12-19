import re

def find_ranges(sensors, row):
    ranges = []
    for sensor, beacon in sensors:
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon
        manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        row_distance = abs(row - sensor_y)
        row_coverage = manhattan_distance - row_distance
        if row_coverage < 0:
            continue
        row_min, row_max = sensor_x - row_coverage, sensor_x + row_coverage
        ranges.append((row_min, row_max))

    ranges.sort()
    current_range = ranges[0]
    merged_ranges = [current_range]
    for range_min, range_max in ranges:
        current_min, current_max = current_range
        if range_min > current_max:
            current_range = (range_min, range_max)
            merged_ranges.append(current_range)
        else:
            current_range = (current_min, max(range_max, current_max))
            merged_ranges[-1] = current_range

    return merged_ranges

def main():
    sensors = []
    with open("15/input") as f:
        for line in f:
            sensor_str, beacon_str = re.findall("x=(-?\d+), y=(-?\d+)", line)
            sensor, beacon = tuple(map(int, sensor_str)), tuple(map(int, beacon_str))
            sensors.append((sensor, beacon))
    
    for i in range(0, 4000000):
        ranges = find_ranges(sensors, i)
        if len(ranges) == 2:
            assert (ranges[0][1] + 2) == ranges[1][0]
            x, y = ranges[0][1] + 1, i
            print((x * 4000000) + y)
            break

if __name__ == "__main__":
    main()