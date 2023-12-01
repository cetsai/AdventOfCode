from __future__ import annotations
import re
import itertools
import numpy as np
from collections import deque
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Valve:
    name: str = ""
    flow_rate: int = 0
    connections: list[str] = field(default_factory=list, compare=False, repr=False)

def shortest_path_length(from_node: Valve, to_node: Valve):
    if from_node == to_node:
        return 0
    horizon = deque()
    horizon.append((from_node, 0))
    visited = set()
    while horizon:
        current_node, distance = horizon.popleft()
        for neighbor in current_node.connections:
            if neighbor == to_node:
                return distance + 1
            if not neighbor in visited:
                horizon.append((neighbor, distance + 1))
        visited.add(current_node)

@dataclass(frozen=True)
class State:
    turn: int = 0
    open_valves: frozenset[str] = {}
    current_location: str = ""

def solution(state: State , memo: dict[State, int]) -> int:
    if state in memo:
        return memo[state]
    return 0
    

def main():
    valve_name = re.compile(r"[A-Z]{2}")
    name_map: dict[str, int] = {}
    valves: list[Valve] = []
    index = 0
    with open("testinput") as f:
        for line in f:
            valve_names = valve_name.findall(line)
            rate = int(re.search("\d+", line).group())
            valve = Valve(name=valve_names[0], flow_rate=rate, connections=valve_names[1:])
            valves.append(valve)
            name_map[valve.name] = index
            index += 1
            
    for valve in valves:
        print(valve)
        for con in valve.connections:
            print("\t" + con)

    num_turns = 30
    max_flow_array: list[int, dict[str, int]] = [0, {} for i in range(len(valves))]
    max_flows: list[int] = [0 for i in range(len(valves))]

    for i in range(len(num_turns)):
        prev_array = max_flow_array.copy()
        for j in range(len(max_flow_array)):
            best_total, valve_open_durations = max_flow_array[j]
            for neighbor in valves[j].connections:
                if name_map[neighbor]:
                    pass

    
    
    """
    key_valves = {valve for name, valve in valves.items() if valve.flow_rate}
    key_valves.add(valves["AA"])
    distances = {}
    for valve1, valve2 in itertools.combinations(key_valves, 2):
        distance = shortest_path_length(valve1, valve2)
        distances[valve1, valve2] = distances[valve2, valve1] = distance
    key_valves.remove(valves["AA"])

    
    result = 0
    current_valve = valves["AA"]
    minutes_remaining = 30
    while key_valves:
        best_valve = (current_valve, 0)
        print(current_valve)
        for valve in key_valves:
            distance = distances[valve, current_valve]
            pressure_released = (minutes_remaining - distance - 1) * valve.flow_rate
            efficiency = pressure_released / distance
            print(pressure_released, distance, valve.name)
            if efficiency > best_valve[1]:
                best_valve = (valve, efficiency)
        current_valve = best_valve[0]
        result += efficiency * distance
        key_valves.remove(current_valve)
    
    print(result)

    """
    """for order in itertools.permutations(key_valves):
        pressure_released = 0
        minutes_remaining = 30
        current_valve = valves["AA"]
        for valve in order:
            distance = distances[current_valve, valve]
            minutes_remaining -= distance + 1
            pressure_released += minutes_remaining * valve.flow_rate
            current_valve = valve
        result = max(result, pressure_released)
    print(result)"""


if __name__ == "__main__":
    main()