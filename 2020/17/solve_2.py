fname = "input.txt"
# fname = "test_input1.txt"

ACTIVE = '#'
INACTIVE = '.'

POCKET_DIMENSION = set()

with open(fname) as fandle:
    for y, line in enumerate(fandle):
        for x, cell in enumerate(line):
            if cell == ACTIVE:
                POCKET_DIMENSION.add((0, x, y, 0))

VECTORS = [
    (w, x, y, z)
    for w in (-1, 0, 1)
    for x in (-1, 0, 1)
    for y in (-1, 0, 1)
    for z in (-1, 0, 1)
    if not all((w==0, x==0, y==0, z==0))
]

def get_neighbours(pocket_dimension, coords):
    global VECTORS

    w, x, y, z = coords

    for dw, dx, dy, dz in VECTORS:
        yield w+dw, x+dx, y+dy, z+dz

def tick(pocket_dimension):
    seen = set()
    new_pocket_dimenson = set()

    stack = list(pocket_dimension)
    while stack:
        seen.add(curr_cell := stack.pop())
        total_living_neighbours = 0

        for neighbor in get_neighbours(pocket_dimension, curr_cell):
            if curr_cell in pocket_dimension and neighbor not in seen:
                stack.append(neighbor)
                seen.add(neighbor)

            if neighbor in pocket_dimension:
                total_living_neighbours += 1

        if curr_cell in pocket_dimension:
            if 2 <= total_living_neighbours <= 3:
                new_pocket_dimenson.add(curr_cell)
        else:
            if total_living_neighbours == 3:
                new_pocket_dimenson.add(curr_cell)

    return new_pocket_dimenson

for i in range(6):
    POCKET_DIMENSION = tick(POCKET_DIMENSION)
print(len(POCKET_DIMENSION))
