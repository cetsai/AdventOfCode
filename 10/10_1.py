import re

def main():
    score = 0
    clock = 1
    register = 1
    with open("10/input") as f:
        command = re.compile(r"addx (-?\d+)$")
        for line in f:
            match = command.match(line)
            score += clock * register if clock % 40 == 20 else 0
            if match:
                clock += 2
                score += (clock - 1) * register if clock % 40 == 21 else 0
                register += int(match.group(1))
            else:
                clock += 1

    print(score)

if __name__ == "__main__":
    main()