FNAME = "input.txt"
# FNAME = "test1.txt"


def get_galaxies():
    with open(FNAME) as fandle:
        return [
            (x, y)
            for y, line in enumerate(fandle)
            for x, cell in enumerate(line)
            if cell == '#'
        ]


def expand_universe(galaxies):
    occupied_cols, occupied_rows = set(), set()
    for x, y in galaxies:
        occupied_cols.add(x)
        occupied_rows.add(y)

    unoccupied_cols = set(range(max(occupied_cols))) - occupied_cols
    unoccupied_rows = set(range(max(occupied_rows))) - occupied_rows

    # maybe this could be made a little more efficient - i.e. not creating
    # new lists of prior points by scanning the unoccupied sets for
    # every galaxy. But I am lazy.        
    factor = 1000000
    factor -= 1
    return [
        (
            galaxy_x + (factor * len([x for x in unoccupied_cols if x < galaxy_x])),
            galaxy_y + (factor * len([y for y in unoccupied_rows if y < galaxy_y])),
        )
        for galaxy_x, galaxy_y in galaxies
    ]

def manhattan_distance(start, end):
    return abs(end[0]-start[0]) + abs(end[1]-start[1])

def main():
    galaxies = get_galaxies()
    expand_galaxies = expand_universe(galaxies)

    # I could use a library itertools.combinations,
    # But I wanna write my own
    total = sum(
        manhattan_distance(
            expand_galaxies[i],
            expand_galaxies[j]
        )
        for i in range(len(galaxies)-1)
        for j in range(i+1, len(galaxies))
    )
    print(total)


if __name__ == "__main__":
    main()