import re

def readInput(stacks, commands):
    with open("input") as f:
        lines = iter(f)
        for line in map(str.rstrip, lines):
            if not line:
                break
            for index, char in enumerate(line):
                if not char.isalpha():
                    continue
                stack = (index // 4) + 1
                if not stack in stacks:
                    stacks[stack] = []
                stacks[stack].append(char)

        for stack in stacks.values():
            stack.reverse()
            
        for line in map(str.rstrip, lines):
            commandregex = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
            match = commandregex.fullmatch(line)
            assert match
            commands.append(tuple(map(int, match.groups())))

def main():
    stacks = {}
    commands = []

    readInput(stacks, commands)

    for num, source, dest in commands:
        for _ in range(num):
            stacks[dest].append(stacks[source].pop())

    stacks = dict(sorted(stacks.items()))
    message = "".join(stack.pop() for stack in stacks.values())
    print(message)


if __name__ == "__main__":
    main()