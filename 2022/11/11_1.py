from dataclasses import dataclass
from typing import Callable
import itertools as it
import re

@dataclass
class Monkey:
    items: list[int] = None
    inspect: Callable[[int], int] = None
    throw: Callable[[int], int] = None
    items_inspected: int = 0

    def read_from_strs(self, strs):
        """Read monkey from string iterator, where each string is a line in the input file"""
        next(strs)  # skip first line ("Monkey #:")

        items_str = next(strs).lstrip().removeprefix("Starting items:")
        self.items = [int(s) for s in items_str.split(",")]
        
        operator, operand =  next(strs).lstrip().removeprefix("Operation: new = old ").split()
        self.inspect = operation(operator, operand)

        divisor, if_true, if_false = (int(re.search(r"\d+", s).group()) for s in it.islice(strs, 3))
        self.throw = test(divisor, if_true, if_false)


def operation(operator, operand):
    operator_map = { "+" : lambda x, y : x + y, "*" : lambda x, y : x * y }
    if operand == "old":
        return lambda x : operator_map[operator](x, x)
    else:
        return lambda x : operator_map[operator](x, int(operand))

def test(divisor, true_res, false_res):
    return lambda x : true_res if x % divisor == 0 else false_res

def main():
    monkeys = []
    with open("input") as f:
        input_iter = it.zip_longest(*([iter(f)] * 7), fillvalue="")
        for lines in input_iter:
            monkey = Monkey()
            monkey.read_from_strs(iter(lines))
            monkeys.append(monkey)
    

    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                inspected_item = monkey.inspect(item)
                bored_item = inspected_item // 3
                target_monkey = monkey.throw(bored_item)
                monkeys[target_monkey].items.append(bored_item)
            monkey.items_inspected += len(monkey.items)
            monkey.items.clear()
    
    first, second = sorted([m.items_inspected for m in monkeys])[-2:]
    print(first * second)

if __name__ == "__main__":
    main()