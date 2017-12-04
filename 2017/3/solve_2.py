with open('input.txt') as fandle:
    target = int(fandle.read())


# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18 5  4  3  12 29
# 40 19 6  1  2  11 28
# 41 20 7  8  9  10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49 50

# Let's just do it dumb and count
def coord_gen():
    x = y = 0
    dx, dy = 0, -1
    while True:
        yield x, -y

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy


def adjacent_cells(loc):
    x, y = loc
    for i in -1, 0, 1:
        for j in -1, 0, 1:
            if i == j == 0:
                continue
            yield x+i, y+j

coord_vals = {(0, 0): 1}


for cell_n, coordinates in enumerate(coord_gen(), 1):
    if cell_n == 1:
        continue

    coord_vals[coordinates] = this_val = sum(
        coord_vals.get(adjacent, 0)
        for adjacent in adjacent_cells(coordinates)
    )


    if this_val > target:
        print this_val
        break

