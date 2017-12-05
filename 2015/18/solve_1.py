fname = 'input.txt'
#fname = 'input_test.txt'
#fname = 'input_test1.txt'
n_steps = 100

with open(fname) as fandle:
    grid = [
        [
            1 if cell == '#' else 0
            for cell in row.strip()
        ]
        for row in fandle
        if row.strip()
    ]

DIMX = len(grid[0])
XMAX = DIMX -1
DIMY = len(grid)
YMAX = DIMY -1

def prt():
    for row in grid:
        print ''.join(str(i) for i in row)


def neighbour_coords(x, y):
    if (x > 0) and (x < XMAX) and (y > 0) and (y < YMAX):
        dxy = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        )

    else:
        dxy = (
            (dx, dy)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if not (
                (dx==dy==0)
                or x+dx > XMAX
                or x+dx < 0
                or y+dy > YMAX
                or y+dy < 0
            )
        )

    for dx, dy in dxy:
        yield x+dx, y+dy

def neighbour_val(x, y):
    return sum(
        grid[_x][_y]
        for _x, _y in neighbour_coords(x, y)
    )

def calc_cell(x, y):
    cell_val = grid[x][y]
    neighbour_total = neighbour_val(x, y)

    if cell_val == 1:
        if (neighbour_total == 2) or (neighbour_total == 3):
            return 1

    if neighbour_total == 3:
        return 1

    return 0


other_grid = [
    [0] * DIMX
    for _ in range(DIMY)
]

for _ in range(n_steps):
    for x in range(DIMX):
        for y in range(DIMY):
            other_grid[x][y] = calc_cell(x, y)
    other_grid, grid = grid, other_grid

#    prt(); print

print sum(sum(row) for row in grid)
