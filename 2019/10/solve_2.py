from fractions import Fraction
from itertools import cycle

FNAME = "input.txt"
# FNAME = "test_1_8.txt"
# FNAME = "test_2_33.txt"
# FNAME = "test_5_210.txt"

def get_asteroids():
    asteroids = set()
    with open(FNAME) as fandle:
        for y, line in enumerate(fandle):
            for x, cell in enumerate(line):
                if cell == '#':
                    asteroids.add((x, y))
    return asteroids
ASTEROIDS = get_asteroids()

def splitsign(i):
    return -1 if i<0 else 1, abs(i)

def angles(ax, ay):
    for ox, oy in ASTEROIDS:
        original_coords = ox, oy
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

        yield ((dx, dy), original_coords)


def get_best_locale_angles():
    max_loc = None
    max_loc_angles = []
    for asteroid in ASTEROIDS:
        this_asteroid_can_see = {}
        for angle, loc in angles(*asteroid):
            if angle not in this_asteroid_can_see:
                this_asteroid_can_see[angle] = [loc]
            else:
                this_asteroid_can_see[angle].append(loc)

        if len(this_asteroid_can_see) > len(max_loc_angles):
            max_loc = asteroid
            max_loc_angles = this_asteroid_can_see

    # sort them so they are in order of closest-to-farthest
    for locs in max_loc_angles.values():
        locs.sort()
    return max_loc_angles

def angle_sortkey(loc):
    ax, ay = loc
    # Yea I'm not proud of this one.
    # first sort by "quadrant"
    # each line x==0 or y==0 (x and y can't be 0 at the same time)
    # belongs to the quadrant to its clockwise
    #      1
    #   8  |  2
    # 7  - + -  3
    #   6  |  4
    #      5
    # If it's on one of the lines then can return just that number.
    if ax == 0:
        return (1,) if ay < 0 else (5,)
    if ay == 0:
        return (3,) if ax > 0 else (7,)

    if ax > 0:
        q = 2 if ay < 0 else 4
    else: # x < 0
        q = 6 if ay > 0 else 8

    #
    ax, ay = abs(ax), abs(ay)
    if q in (2, 6):
        frac = Fraction(ax, ay)
    else: # q in (4, 8)
        frac = Fraction(ay, ax)


    return (q,frac)


# This is horribly inefficient
angles = get_best_locale_angles()
sorted_angles = sorted(angles, key=angle_sortkey)
n_found = 0
LOOKING_FOR = 200
while sorted_angles:
    sorted_angles = [i for i in sorted_angles if angles[i]]
    for angle in sorted_angles:
        n_found += 1
        this_angle = angles[angle].pop(0)
        if n_found == LOOKING_FOR:
            print(this_angle[0]*100 + this_angle[1])
            exit(0) # I am lazy

print("ruh-roh")
