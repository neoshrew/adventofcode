from itertools import combinations

FNAME = "input.txt"
# FNAME = "test1.txt"

def get_grid():
    antennas = {}
    x, y = 0, 0
    with open(FNAME) as fandle:
        for y, row in enumerate(fandle):
            row = row.strip()
            if not row:
                continue
            for x, cell in enumerate(row):
                if cell != '.':
                    if cell not in antennas:
                        antennas[cell] = []
                    antennas[cell].append((x, y))
    
    return antennas, (x+1, y+1)


def main():
    antennas, (width, height) = get_grid()

    antinodes = set()

    def in_grid(loc):
        return 0 <= loc[0] < width and 0 <= loc[1] < height

    for freq, locs in antennas.items():
        for loca, locb in combinations(locs, 2):
            # Vector from B to A
            vec = loca[0]-locb[0], loca[1]-locb[1]

            # Follow the line onward from A
            loc = loca
            while in_grid(loc):
                antinodes.add(loc)
                loc = loc[0]+vec[0], loc[1]+vec[1]

            # Follow the line onward from B
            loc = locb
            while in_grid(loc):
                antinodes.add(loc)
                loc = loc[0]-vec[0], loc[1]-vec[1]


    print(len(antinodes))


if __name__ == "__main__":
    main()