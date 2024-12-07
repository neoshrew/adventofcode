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


def main():
    obstacles, guard, dimensions = get_input()
    direction = 0, -1

    visited_locations = set()
    visited_locations.add(guard)
    while True:
        new_loc = guard[0]+direction[0], guard[1]+direction[1]
        if not 0 <= new_loc[0] < dimensions[0] or not 0 <= new_loc[1] < dimensions[1]:
            break

        if new_loc in obstacles:
            direction = {
                (0, -1) : (1, 0),
                (1, 0) : (0, 1),
                (0, 1) : (-1, 0),
                (-1, 0) : (0, -1),
            }[direction]
        else:
            guard = new_loc
            visited_locations.add(guard)
        
    print(len(visited_locations))

if __name__ == "__main__":
    main()