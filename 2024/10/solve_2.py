FNAME = "input.txt"
# FNAME = "test1.txt"

def get_grid():
    grid = {}
    with open(FNAME) as fandle:
        for y, row in enumerate(fandle):
            row = row.strip()
            if not row:
                continue
            for x, cell in enumerate(row):
                grid[x,y] = int(cell)

    return grid


VECS = [
    (-1, 0), # left
    (0, -1), # up
    (1, 0), # right
    (0, 1), # down
]

def main():
    grid = get_grid() 

    # Start from the ends and work out way back.
    
    scores = {}
    for coord, cell in grid.items():
        if cell not in scores:
            scores[cell] = {}
        # Each 9 can only get to that 9
        if cell == 9:
            scores[cell][coord] = 1
        else:
            scores[cell][coord] = None

    for i in range(8, -1, -1):
        for (x, y) in scores[i]:
            scores[i][x,y] = sum(
                scores[i+1].get((x+dx, y+dy), 0)
                for (dx, dy) in VECS
            )


    total = sum(scores[0].values())
    print(total)

if __name__ == "__main__":
    main()