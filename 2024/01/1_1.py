def main():
    left = []
    right = []
    with open("input") as f:
        for line in f:
            l, r = tuple(map(int, line.split()))
            left.append(l)
            right.append(r)

    left.sort()
    right.sort()

    sum = 0
    for l,r in zip(left, right):
        sum += abs(l - r)
    print(sum)

if __name__ == "__main__":
    main()