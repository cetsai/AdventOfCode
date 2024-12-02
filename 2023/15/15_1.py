
def ascii_code(string: str):
    result = 0
    for char in string:
        result = result + ord(char)
        result = result * 17 % 256
    return result


def main():
    steps: list[str]
    with open("input") as f:
        steps = f.readline().rstrip().split(',')
    result = 0
    for step in steps:
        result += ascii_code(step)
    print(result)


if __name__ == "__main__":
    main()
