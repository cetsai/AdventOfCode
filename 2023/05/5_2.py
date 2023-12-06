"""
Instead of viewing these as mappings, we can view them as function sets
which apply addition to an input domain. This way, combining mappings
becomes conceptually easier as it boils down to a range overlap problem
with some addition for the intersection.

if we always use the range with the lowest start first, we have 3 cases:
-===--------
------===---
B.min > A.max

-======-----
-----======-
B.min < A.max < B.max

-==========-
---====-----
B.max < A.max

Disjoint ranges stay as two disjoint ranges, and any overlaps become up
to three ranges

As an optimization we can also order the sub-mappings by the source
ranges so the lookup can become a binary search.

"""

from __future__ import annotations
import re
import itertools as it
from dataclasses import dataclass, field
from functools import cmp_to_key

@dataclass
class MapEntry:
    source: range
    addend: int

    def __init__(self, dest_start, source_start, length):
        self.source = range(source_start, source_start + length)
        self.destination = range(dest_start, dest_start + length)

    @staticmethod
    def map_entrycmp(left: MapEntry, right: MapEntry)
        if left.source[0] < right.source[0]:
            return -1
        if right.source[0] < left.source[0]:
            return 1
        if left.source[-1] < right.source[-1]:
            return -1
        if right.source[-1] < left.source[-1]:
            return 1
        return 0


@dataclass
class Map:
    entries: list[MapEntry] = field(default_factory=list)
    
    @staticmethod
    def combine(left: Map, right: Map):
        combined_ranges = sorted(left.entries + right.entries)
        pass

    def map(self, source_value: int) -> int:
        for entry in self.entries:
            if source_value in entry.source:
                return entry.destination[source_value - entry.source[0]]
        return source_value


def main():
    almanac: list[Map] = []
    seed_ranges = []
    with open("input") as f:
        seeds_in = list(map(int, re.findall(r"\d+", f.readline())))
        for start, length in it.batched(seeds_in, 2):
            seed_ranges.append(range(start, start + length))
        reading_map = False
        current_map = Map()
        for line in f:
            map_values = list(map(int, re.findall(r"\d+", line)))
            if map_values:
                reading_map = True
                dest, source, length = map_values
                current_map.entries.append(MapEntry(dest, source, length))
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
