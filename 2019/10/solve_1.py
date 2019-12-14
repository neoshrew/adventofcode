from fractions import Fraction

asteroids = set()

fname = "input.txt"
# fname = "test_1_8.txt"
# fname = "test_2_33.txt"
# fname = "test_5_210.txt"

with open(fname) as fandle:
    for y, line in enumerate(fandle):
        for x, cell in enumerate(line):
            if cell == '#':
                asteroids.add((x, y))


def splitsign(i):
    return -1 if i<0 else 1, abs(i)


max_can_see = 0

for ax, ay in asteroids:
    this_asteroid_angles = set()
    for ox, oy in asteroids:
        dx, dy = ox - ax, oy - ay
        if dx == dy == 0:
            continue

        dxs, dx = splitsign(dx)
        dys, dy = splitsign(dy)

        if dy == 0:
            dx = 1
        elif dx == 0:
            dy = 1
        else:
            as_fac = Fraction(dx, dy)
            dx = as_fac.numerator
            dy = as_fac.denominator

        dx *= dxs
        dy *= dys

        this_asteroid_angles.add((dx, dy))

    this_asteroid_can_see = len(this_asteroid_angles)
    if this_asteroid_can_see > max_can_see:
        max_can_see = this_asteroid_can_see

print(max_can_see)
