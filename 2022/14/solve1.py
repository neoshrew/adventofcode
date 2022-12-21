INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

ROCK = "#"
SAND = "o"
AIR = "."
START = "+"
SAND_START = (500,0)


def get_grid():
    grid = {
        SAND_START: START,
    }

    with open(INPUT_FNAME) as fandle:
        # 503,4 -> 502,4 -> 502,9 -> 494,9
        for line in fandle:
            points = [
                tuple(int(i) for i in point_raw.split(","))
                for point_raw in line.strip().split(" -> ")
            ]
            point_pairs = (
                (points[i], points[i+1])
                for i in range(len(points)-1)
            )
            for (startx, starty), (endx, endy) in point_pairs:
                if startx == endx:
                    starty, endy = min(starty, endy), max(starty, endy)
                    for y in range(starty, endy+1):
                        grid[startx, y] = ROCK
                else:
                    startx, endx = min(startx, endx), max(startx, endx)
                    for x in range(startx, endx+1):
                        grid[x, starty] = ROCK
    return grid

def print_grid(grid):
    minx = min(i[0] for i in grid) -1
    maxx = max(i[0] for i in grid) +1
    miny = 0
    maxy = max(i[1] for i in grid) +1
    
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(grid.get((x, y), AIR), end="")
        print()

def main():
    grid = get_grid()

    directions = [
        (0, 1), # Falls down if it can
        (-1, 1), # Then tries down and to the left
        (1, 1), # Then tries down and to the right
    ]

    maxy = max(i[1] for i in grid)
    total = 0

    path_stack = [SAND_START]
    while path_stack:
        curr = path_stack[-1]

        if curr[1] >= maxy:
            # We're at the same depth as the lowest piece of rock
            # or lower, so we're going to fall forever.
            # This is our search condition.
            break

        for dir in directions:
            target = curr[0]+dir[0], curr[1]+dir[1]
            # For now if it's populated it's rock or sand
            if target not in grid:
                # We can move in this direction, so move that way
                path_stack.append(target)
                break

        else:
            # We didn't move in any direction, so mark this as sand
            # and then move back up our current search path
            grid[curr] = SAND
            path_stack.pop()
            total += 1

    print(total)


if __name__ == "__main__":
    main()