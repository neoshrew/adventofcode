FNAME = "input.txt"
# FNAME = "test1.txt"
# FNAME = "test3.txt"
# FNAME = "test4.txt"
# FNAME = "test5.txt"
# FNAME = "test6.txt"


NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
SYMBOL_VECTORS = {
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
                if cell in SYMBOL_VECTORS:
                    grid[x, y] = {
                        (x+dx, y+dy)
                        for dx, dy in SYMBOL_VECTORS[cell]
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


VECTORS = set(
    (dx, dy)
    for dx in range(-1, 2)
    for dy in range(-1, 2)
    if not dx == dy == 0
)
def get_points_around(coord):
    return {
        (coord[0]+dx, coord[1]+dy)
        for dx, dy in VECTORS
    }


def get_fill(origin, taken, bounds):
    def outside_bounds(coord):
        nonlocal bounds
        ((min_x, min_y), (max_x, max_y)), (x, y) = bounds, coord
        # Give ourselves a margin of 1 so we can fill around the pipes
        return any((x<min_x-1, x>max_x+1, y<min_y-1, y>max_y+1))

    outside = False

    todo = set([origin])
    fill_coords = set()
    seen = set(taken)
    while todo:
        curr = todo.pop()
        seen.add(curr)
        if outside_bounds(curr):
            outside = True

        else:
            fill_coords.add(curr)
            todo.update(get_points_around(curr)-seen)


    return fill_coords, outside

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

    # The only way I can think of doing this is to "double" the
    # resolution of our grid, and make the current pipe coordinates
    # the "middle" of a pipe section, and then have "connections" between 
    # pipes as items on the grid. Then we can use a graph search
    # fill algorithm to find counts of caught/not caught.
    # This is not very memory efficient.

    # We don't care about order for the new path, just holding "middle"s and
    # "connection"s that comprise the path, to block our fill.
    new_path = set()
    new_start = (start[0]*2, start[1]*2)
    for i in range(len(path)):
        curr = path[i]
        next_ = path[i+1 if i+1 < len(path) else 0]
        curr = curr[0]*2, curr[1]*2
        next_ = next_[0]*2, next_[1]*2
        new_path.add(curr)
        new_path.add(
            (
                (curr[0] + next_[0])//2,
                (curr[1] + next_[1])//2,
            )
        )
    
    # We only care about stuff inside our pipe, so limit our scope to coordinates
    # that are within a bounding box of our pipe
    bounds = (
        (
            min(x for x, _ in new_path),
            min(y for _, y in new_path),
        ),
        (
            max(x for x, _ in new_path),
            max(y for _, y in new_path),
        ),
    )

    to_check = get_points_around(new_start) - new_path
    while to_check:
        check = next(iter(to_check))
        fill, outside = get_fill(check, set(new_path), bounds)

        if outside:
            to_check -= fill
        else:
            break

    # Now we only want cells that are on even coordinates.
    surrounded_cells = set(
        coord
        for coord in fill
        if coord[0]%2 == coord[1]%2 == 0
    )

    print(len(surrounded_cells))



if __name__ == "__main__":
    main()