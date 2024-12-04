import itertools as it

def main():
    grid = []
    with open("input") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(char)
            grid.append(row)
    
    def check_cell(x:int, y:int):
        if grid[x][y] != 'A':
            return 0
        a = grid[x-1][y-1]
        b = grid[x+1][y-1]
        c = grid[x-1][y+1]
        d = grid[x+1][y+1]
        if a + d != "MS" and a + d != "SM":
            return 0
        if b + c != "MS" and b + c != "SM":
            return 0
        return 1
                    
    sum = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            sum += check_cell(x, y)
    print(sum)



if __name__ == "__main__":
    main()