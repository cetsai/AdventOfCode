def main():
    total = 0

    with open("3/input") as f:
        for line in [l.rstrip() for l in f]:
            first = line[:len(line)//2]
            second = line[len(line)//2:]
            
            # originally used list comprehension, but this is way cleaner
            [item] = set(first) & set(second)
            ordinal = (ord(item) - ord("a")) if item.islower() else (ord(item) - ord("A"))
            priority = ordinal + (1 if item.islower() else 27)
            total += priority

    print(total)

if __name__ == "__main__":
    main()