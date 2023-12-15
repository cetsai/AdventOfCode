

def main():
    patterns = list()
    with open("testinput") as f:
        pattern = list()
        for line in map(str.rstrip, f):
            if not line:
                patterns.append(pattern)
                pattern = list()
            else:
                pattern.append(list(line))

    print(patterns)
    for pattern in patterns:
        for row in pattern:
            pass


if __name__ == "__main__":
    main()
