"""
Instead of tracking a single path, every node whose label ends in 'A' is
the start of a different path. The task is to find the earliest step
at which all paths are on nodes whose labels end in 'Z'.

Similar to part 1, but we do it for every path. Once we've found the
step count of each individual path, we can get the answer by taking the
least common multiple fo the step counts, rather than having to
conintually loop through the instructions until all paths line up.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import cycle
import re
import math


@dataclass(slots=True, frozen=True)
class Node:
    name: str
    left: str
    right: str


def main():
    nodes:dict[str, Node] = {}
    instructions = []
    with open("input") as f:
        instructions = f.readline().rstrip()
        node_pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
        for line in f:
            node_input = node_pattern.fullmatch(line.rstrip())
            if node_input:
                name, left, right = node_input.groups()
                nodes[name] = Node(name, left, right)

    current_nodes = [(x, 0) for x in nodes.values() if x.name[-1] == 'A']
    step_counts = []
    for step in cycle(instructions):
        if not current_nodes:
            break
        next_nodes = []
        for node, step_count in current_nodes:
            if node.name[-1] == 'Z':
                step_counts.append(step_count)
                continue
            if step == 'R':
                next_nodes.append((nodes[node.right], step_count + 1))
            elif step == 'L':
                next_nodes.append((nodes[node.left], step_count + 1))
            else:
                print(step)
                break
        current_nodes = next_nodes
    print(math.lcm(*step_counts))


if __name__ == "__main__":
    main()
