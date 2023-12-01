import re

def main():
    sensors = []
    with open("input") as f:
        for line in f:
            sensor_str, beacon_str = re.findall("x=(-?\d+), y=(-?\d+)", line)
            sensor, beacon = tuple(map(int, sensor_str)), tuple(map(int, beacon_str))
            sensors.append((sensor, beacon))
    
    ranges = []
    target_row = 2000000
    for sensor, beacon in sensors:
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon
        manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        row_distance = abs(target_row - sensor_y)
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

    beacons = {b for _, b in sensors if b[1] == target_row}
    total_coverage = -len(beacons)
    for range_min, range_max in merged_ranges:
        total_coverage += range_max - range_min + 1
    print(total_coverage)

if __name__ == "__main__":
    main()