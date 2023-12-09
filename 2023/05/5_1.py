import re
from dataclasses import dataclass, field


@dataclass
class MapEntry:
    source: range
    destination: range

    def __init__(self, dest_start, source_start, length):
        self.source = range(source_start, source_start + length)
        self.destination = range(dest_start, dest_start + length)


@dataclass
class Map:
    entries: list[MapEntry] = field(default_factory=list)

    def map(self, source_value: int) -> int:
        for entry in self.entries:
            if source_value in entry.source:
                return entry.destination[source_value - entry.source[0]]
        return source_value


def main():
    almanac: list[Map] = []
    seeds = []
    with open("input") as f:
        seeds = list(map(int, re.findall(r"\d+", f.readline())))
        reading_map = False
        current_map = Map()
        for line in f:
            map_values = list(map(int, re.findall(r"\d+", line)))
            if map_values:
                reading_map = True
                dest, source, length = map_values
                current_map.entries.append(
                    MapEntry(dest, source, length)
                )
            elif reading_map:
                reading_map = False
                almanac.append(current_map)
                current_map = Map()
        almanac.append(current_map)

    for almanac_map in almanac:
        seeds = list(map(almanac_map.map, seeds))

    print(min(seeds))


if __name__ == "__main__":
    main()
