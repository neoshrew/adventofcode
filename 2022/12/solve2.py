INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

HEIGHTS = {c: h for (h, c) in enumerate(chr(i) for i in range(ord('a'), ord('z')+1))}
HEIGHTS["S"] = HEIGHTS["a"]
HEIGHTS["E"] = HEIGHTS["z"]

def main():
    end = None
    grid = {}

    with open(INPUT_FNAME) as fandle:
        for Y, line in enumerate(fandle):
            line = line.strip()
            for X, cell in enumerate(line):
                grid[X, Y] = HEIGHTS[cell]

                if cell == "E":
                    end = (X, Y)

    queue = [end]
    seen = set(queue)
    scores = {end: 0}

    while queue:
        curr = queue.pop(0)
        for neighbour in get_neighbours(curr, grid):
            if neighbour in seen:
                continue
            if (grid[curr] - grid[neighbour]) <= 1:
                scores[neighbour] = scores[curr] + 1
                seen.add(neighbour)
                queue.append(neighbour)

            if grid[curr] == HEIGHTS["a"]:
                print(scores[curr])
                return


def get_neighbours(coord, grid):
    x, y = coord
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x+dx, y+dy
        if (nx, ny) in grid:
            yield nx, ny


if __name__ == "__main__":
    main()