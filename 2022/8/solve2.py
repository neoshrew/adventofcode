INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

def get_grid():
    with open(INPUT_FNAME) as fandle:
        return [
            line.strip()
            for line in fandle
        ]


def main():
    grid = get_grid()
    width, height = len(grid[0]), len(grid)

    # Just do a big ol' dumb O(X^3)
    def taller_this_way(coords):
        nonlocal grid, width, height
        nonlocal cell
        retval = 0
        for x, y in coords:
            retval += 1
            if grid[y][x] >= cell:
                break
        return retval


    # skip the edges tho
    max_score = 0
    for y in range(1, height):
        for x in range(1, width):
            cell = grid[y][x]

            above = taller_this_way((x, dy) for dy in range(y-1, -1, -1))
            below = taller_this_way((x, dy) for dy in range(y+1, height))
            left = taller_this_way((dx, y) for dx in range(x-1, -1, -1))
            right = taller_this_way((dx, y) for dx in range(x+1, width))
            score = above * below * left * right
            if score > max_score:
                max_score = score
    print(max_score)


if __name__ == "__main__":
    main()
