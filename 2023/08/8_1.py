"""
https://adventofcode.com/2023/day/8

The first line of the input is a series of 'R' and 'L' characters, which
represents a series of instructions. For the rest of the input, each
line represents a node with a label and two neighbors, left and right.
The task is to find how many steps it would take to go from node "AAA"
to node "ZZZ" by only following the given instructions (repeating if
needed).

My solution constructs node objects from the input. Then, I continually
loop through the instructions until "ZZZ" is reached, incrementing a
step count along the way.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import cycle
import re
import math


@dataclass
class Node:
    left: str
    right: str


def main():
    nodes = {}
    instructions = []
    with open("input") as f:
        instructions = f.readline().rstrip()
        node_pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
        for line in f:
            node_input = node_pattern.fullmatch(line.rstrip())
            if node_input:
                name, left, right = node_input.groups()
                nodes[name] = Node(left, right)

    current_node = nodes["AAA"]
    step_count = 0
    for instruction in cycle(instructions):
        if current_node is nodes["ZZZ"]:
            break
        if instruction == 'R':
            current_node = nodes[current_node.right]
        elif instruction == 'L':
            current_node = nodes[current_node.left]
        else:
            print(instruction)
            break
        step_count += 1
    print(step_count)


if __name__ == "__main__":
    main()
