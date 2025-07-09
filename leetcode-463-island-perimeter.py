def islandPerimeter(grid: list[list[int]]) -> int:
    def find_land(grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    return (y, x)

    level = [find_land(grid)]
    print(f"initial level={level}")
    p = 0
    while len(level) > 0:
        next_level = []
        for s in level:
            y, x = s
            if grid[y][x] == 2:
                continue
            grid[y][x] = 2
            print(f"p={p}, x={x}, y={y}, grid={grid}, level={level}")
            if x > 0:
                if grid[y][x - 1] == 0:
                    p += 1
                elif grid[y][x - 1] == 1:
                    next_level.append([y, x - 1])
            else:
                p += 1
            if x + 1 < len(grid[y]):
                if grid[y][x + 1] == 0:
                    p += 1
                elif grid[y][x + 1] == 1:
                    next_level.append([y, x + 1])
            else:
                p += 1
            if y > 0:
                if grid[y - 1][x] == 0:
                    p += 1
                elif grid[y - 1][x] == 1:
                    next_level.append([y - 1, x])
            else:
                p += 1
            if y + 1 < len(grid):
                if grid[y + 1][x] == 0:
                    p += 1
                elif grid[y + 1][x] == 1:
                    next_level.append([y + 1, x])
            else:
                p += 1
        level = next_level
    return p


print(islandPerimeter(grid=[[1,1],[1,1]]))