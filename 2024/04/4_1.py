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
        sum = 0
        for x_dir, y_dir in it.product([-1, 0, 1], repeat=2):
            for dist, letter in zip(range(4), "XMAS"):
                x_offset = x_dir * dist
                y_offset = y_dir * dist
                x_pos = x + x_offset
                y_pos = y + y_offset
                if x_pos not in range(len(grid))\
                   or y_pos not in range(len(grid[0]))\
                   or grid[x_pos][y_pos] != letter:
                    break
            else:
                sum += 1

        return sum
                    
    sum = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            sum += check_cell(x, y)
    print(sum)



if __name__ == "__main__":
    main()