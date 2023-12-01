import re
import numpy as np

def main():
    register = 1
    command_cycles = 0
    display = np.zeros((6, 40))
    command = re.compile(r"addx (-?\d+)$")
    match = None
    with open("10/input") as f:
        file_iter = iter(f)
        for clock in range(240):
            if not command_cycles and match:
                register += int(match.group(1))

            if clock % 40 >= register - 1 and clock % 40 <= register + 1:
                display[clock//40, clock%40] = 1

            if not command_cycles:
                try:
                    match = command.match(next(file_iter))
                    command_cycles = 2 if match else 1
                except StopIteration:
                    assert False

            command_cycles -= 1

    for row in display:
        for pixel in row:
            print("#" if pixel else ".", end="")
        print()

if __name__ == "__main__":
    main()