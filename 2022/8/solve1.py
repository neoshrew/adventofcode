INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

def get_grid():
    with open(INPUT_FNAME) as fandle:
        return [
            line.strip()
            for line in fandle
        ]

def print_grid(grid, can_see):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in can_see:
                print(cell, end="")
            else:
                print(" ", end="")
        print()

def main():
    grid = get_grid()
    can_see = set()
    x, y = len(grid[0]), len(grid)

    def visible_on_line(coords):
        nonlocal grid, can_see
        x, y = next(coords)
        can_see.add((x, y))
        maxsofar = grid[y][x]
        for x, y in coords:
            if grid[y][x] > maxsofar:
                maxsofar = grid[y][x]
                can_see.add((x, y))

    for dx in range(x):
        visible_on_line((dx, dy) for dy in range(y))
        visible_on_line((dx, dy) for dy in range(y-1, -1, -1))

    for dy in range(y):
        visible_on_line((dx, dy) for dx in range(x))
        visible_on_line((dx, dy) for dx in range(x-1, -1, -1))

    # print_grid(grid, can_see)
    print(len(can_see))

if __name__ == "__main__":
    main()
