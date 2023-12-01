def main():
    total = 0
    with open("input") as f:
        for elves in zip(*([iter(f)] * 3), strict=True):
            elves = [elf.rstrip() for elf in elves]
            [badge] = set(elves[0]) & set(elves[1]) & set(elves[2])

            ordinal = (ord(badge) - ord("a")) if badge.islower() else (ord(badge) - ord("A"))
            priority = ordinal + (1 if badge.islower() else 27)
            total += priority

    print(total)
            

if __name__ == "__main__":
    main()