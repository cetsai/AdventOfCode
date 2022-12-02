elves = []
calories = []

with open("1/input.txt") as f:
    for line in f:
        if(line.rstrip() == ""):
            elves.append(calories)
            calories = []
        else:
            calories.append(int(line))

print(max([sum(l) for l in elves]))