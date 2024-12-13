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

    for freq, locs in antennas.items():
        for loca, locb in combinations(locs, 2):
            # Vector from B to A
            vec = loca[0]-locb[0], loca[1]-locb[1]

            # Location after A on the line B->A
            an1 = loca[0]+vec[0], loca[1]+vec[1]
            if 0 <= an1[0] < width and 0 <= an1[1] < height:
                antinodes.add(an1) 

            # Location after B on the line A->B
            an2 = locb[0]-vec[0], locb[1]-vec[1]
            if 0 <= an2[0] < width and 0 <= an2[1] < height:
                antinodes.add(an2) 

    print(len(antinodes))


if __name__ == "__main__":
    main()