with open("input.txt") as fandle:
    coords_1 = fandle.readline().strip().split(',')
    coords_2 = fandle.readline().strip().split(',')

# coords_1 = "R8,U5,L5,D3".split(',')
# coords_2 = "U7,R6,D4,L4".split(',')

VECS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}
def get_all_points(coords):
    points = set()
    currx = curry = 0

    coords = coords[::-1]
    while coords:
        curr_coord = coords.pop()
        dir, dist_raw = curr_coord[0], curr_coord[1:]
        dx, dy = VECS[dir]

        for _ in range(int(dist_raw)):
            currx, curry = currx+dx, curry+dy
            points.add((currx, curry))

    return points

points_1 = get_all_points(coords_1)
points_2 = get_all_points(coords_2)

crossover_points = points_1 & points_2

crossover_distances = [abs(i[0])+abs(i[1]) for i in crossover_points]
print(sorted(crossover_distances)[0])
