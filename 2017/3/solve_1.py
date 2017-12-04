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


for cell_n, coordinates in enumerate(coord_gen(), 1):
    if cell_n == target:
        break

print sum(abs(i) for i in coordinates)