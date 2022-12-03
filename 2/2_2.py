def main():
    scores = [[4, 8, 3],
              [1, 5, 9],
              [7, 2, 6]]

    mapping = {
        "X": 0,
        "Y": 1,
        "Z": 2,
        "A": 0,
        "B": 1,
        "C": 2,
    }

    total = 0

    with open("2/input") as f:
        for line in f:
            first, second = [mapping[c] for c in line.split()]
            total += sorted(scores[first])[second]

    print(total)

if __name__ == "__main__":
    main()