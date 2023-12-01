def main():
    grid = []
    with open("input") as f:
        for line in f:
            row = []
            for char in line.rstrip():
                row.append(int(char))
            grid.append(row)

    height = len(grid)
    width = len(grid[0])
    visibility = [[0] * width for _ in range(height)]

    
    umax = [-1] * width
    dmax = [-1] * width
    for i in range(height):
        lmax = -1
        rmax = -1
        for j in range(width):
            ultree = grid[i][j]
            drtree = grid[-i-1][-j-1]
            if ultree > umax[j]:
                umax[j] = ultree
                visibility[i][j] = 1
            if ultree > lmax:
                lmax = ultree
                visibility[i][j] = 1
            if drtree > dmax[j]:
                dmax[j] = drtree
                visibility[-i-1][-j-1] = 1
            if drtree > rmax:
                rmax = drtree
                visibility[-i-1][-j-1] = 1
        
    print(sum(sum(tree) for tree in visibility))

if __name__ == "__main__":
    main()