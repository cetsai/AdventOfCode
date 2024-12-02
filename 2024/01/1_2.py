from collections import Counter

def main():
    left = []
    right = Counter()
    with open("input") as f:
        for line in f:
            l, r = tuple(map(int, line.split()))
            left.append(l)
            right[r] += 1

    sum = 0
    for l in left:
        sum += l * right[l]
    print(sum)

if __name__ == "__main__":
    main()