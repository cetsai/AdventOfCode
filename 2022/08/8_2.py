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
    scores = [[1] * width for _ in range(height)]
    views = [[0] * 10 for _ in range(4)]

    for idx in range(width * height):
        for direction in range(len(views)):
            coord = [0,0]
            dim = height if direction // 2 == 0 else width
            coord[0] = idx // width if direction // 2 == 0 else idx % height
            coord[1] = idx % width if direction // 2 == 0 else idx // height
            coord[0] = coord[0] if direction % 2 == 0 else -coord[0] - 1
            coord[1] = coord[1] if direction % 2 == 0 else -coord[1] - 1
            tree = grid[coord[0]][coord[1]]
            if idx % dim == 0:
                views[direction] = [0] * 10
            scores[coord[0]][coord[1]] *= views[direction][tree]
            views[direction] = [v + 1 if i > tree else 1 for i, v in enumerate(views[direction])]
    
    print(max([max(s) for s in scores]))

if __name__ == "__main__":
    main()