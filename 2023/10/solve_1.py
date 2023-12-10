FNAME = "input.txt"
# FNAME = "test1.txt"
# FNAME = "test2.txt"

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
VECTORS = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
}

def get_grid():
    grid = {}
    start = None
    with open(FNAME) as fandle:
        for y, line in enumerate(fandle):
            for x, cell in enumerate(line.strip()):
                if cell in VECTORS:
                    grid[x, y] = {
                        (x+dx, y+dy)
                        for dx, dy in VECTORS[cell]
                    }
                if cell == "S":
                    start = (x, y)

    # Assuming that AoC is nice, and only the relevant pipes will
    # try to connect to our Start.
    # If this isn't the case, then we'd just have to walk all connected
    # directions.
    grid[start] = set(
        neighbour
        for neighbour in (
            (start[0]+dx, start[1]+dy)
            for dx, dy in (NORTH, EAST, SOUTH, WEST)
        )
        if start in grid.get(neighbour, {})
    )
    if len(grid[start]) != 2:
        raise Exception("len(start_connections) == {}".format(len(grid[start])))

    return start, grid

def main():
    start, grid = get_grid()
    path = [start]

    while True:
        path.append(
            next(iter(
                grid[path[-1]] - set(path[-2:])
            ))
        )
        if path[-1] == start:
            break

    print(len(path)//2)
        

if __name__ == "__main__":
    main()