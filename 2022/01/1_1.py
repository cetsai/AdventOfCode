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

    print(max([sum(l) for l in elves]))

if __name__ == "__main__":
    main()