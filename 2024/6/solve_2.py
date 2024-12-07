FNAME = "input.txt"
# FNAME = "test1.txt"

def get_input():
    obstacles = set()
    guard = None
    dimensions = (0, 0)
    with open(FNAME) as fandle:
        for y, row in enumerate(fandle):
            if not row.strip():
                continue
            for x, cell in enumerate(row):
                if cell == "#":
                    obstacles.add((x, y))
                elif cell == "^":
                    guard = x, y

                dimensions = x+1, y+1

    return obstacles, guard, dimensions


def walk(obstacles, guard, dimensions):
    direction = 0, -1

    visited_locations = set()
    visited_locations.add((guard, direction))
    while True:
        new_loc = guard[0]+direction[0], guard[1]+direction[1]
        if not 0 <= new_loc[0] < dimensions[0] or not 0 <= new_loc[1] < dimensions[1]:
            return set(vl[0] for vl in visited_locations), False

        if (new_loc, direction) in visited_locations:
            return set(vl[0] for vl in visited_locations), True

        if new_loc in obstacles:
            direction = {
                (0, -1) : (1, 0),
                (1, 0) : (0, 1),
                (0, 1) : (-1, 0),
                (-1, 0) : (0, -1),
            }[direction]
        else:
            guard = new_loc
            visited_locations.add((guard, direction))



def main():
    obstacles, guard, dimensions = get_input()

    original_walk_locations, _ = walk(obstacles, guard, dimensions)
    original_walk_locations.remove(guard)

    # Only places we could put an obstacle are in the original path
    # of the guard. So lets just try all of them.
    total = 0
    for new_obstacle in original_walk_locations:
        obstacles.add(new_obstacle)
        _, looped = walk(obstacles, guard, dimensions)
        obstacles.remove(new_obstacle)
        if looped:
            total += 1

    print(total)

if __name__ == "__main__":
    main()