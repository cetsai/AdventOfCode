def main():
    elves = []
    calories = []

    with open("input") as f:
        for line in f:
            if(line.rstrip() == ""):
                elves.append(calories)
                calories = []
            else:
                calories.append(int(line))

    print(sum((sorted([sum(e) for e in elves])[-3:])))

if __name__ == "__main__":
    main()