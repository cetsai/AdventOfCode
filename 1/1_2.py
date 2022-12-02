elves = []
calories = []

with open("1/input.txt") as f:
    for line in f:
        if(line.rstrip() == ""):
            elves.append(calories)
            calories = []
        else:
            calories.append(int(line))

print(sum((sorted([sum(e) for e in elves])[-3:])))