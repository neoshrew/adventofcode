from copy import deepcopy

fname = "input.txt"
# fname = "test_input1.txt"

OCCUPIED = "#"
VACANT = "L"
FLOOR = "."

with open(fname) as fandle:
    GRID = [
        list(line.rstrip())
        for line in fandle
    ]

def pg(grid):
    print("\n".join("".join(row) for row in grid))
    print()

def get_neighbour_count(grid, x, y):
    total = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0: continue
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0: continue
            try:
                if grid[x+dx][y+dy] == OCCUPIED:
                    total += 1
            except IndexError:
                pass
    return total

def transition_grid(grid, new_grid=None):
    if new_grid is None:
        new_grid = deepcopy(grid)

    has_changed = False

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == FLOOR:
                new_grid[x][y] = FLOOR
            else:
                nc = get_neighbour_count(grid, x, y)
                if cell == VACANT and nc == 0:
                    new_grid[x][y] = OCCUPIED
                    has_changed = True
                elif cell == OCCUPIED and nc >= 4:
                    new_grid[x][y] = VACANT
                    has_changed = True
                else:
                    new_grid[x][y] = cell

    return new_grid, has_changed

OGRID = None
while True:
    (GRID, changed), OGRID = transition_grid(GRID, OGRID), GRID
    if not changed:
        break

print(sum(row.count(OCCUPIED) for row in GRID))
