
def adjacent(char):
    match char:
        case '-':
            return None

def main():
    grid = []
    with open("testinput") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(char)
            grid.append(row)

    print(grid)



if __name__ == "__main__":
    main()