FNAME = "input.txt"
# FNAME = "test1.txt"

def get_garden():
    garden = {}
    with open(FNAME) as fandle:
        for y, row in enumerate(fandle):
            row = row.strip()
            if not row:
                continue
            for x, plot in enumerate(row):
                garden[x, y] = plot

    return garden

VECS = {
    "W": (-1, 0), # left
    "N": (0, -1), # up
    "E": (1, 0), # right
    "S": (0, 1), # down
}
def main():
    garden = get_garden()

    areas = []
    while garden:
        starter = next(iter(garden))
        plant_type = garden.pop(starter)
        searching = [starter]
        this_area = set(searching)
        areas.append(this_area)

        while searching:
            x, y = searching.pop()
            for dx, dy in VECS.values():
                search_coord = (x+dx, y+dy)
                if garden.get(search_coord) == plant_type:
                    searching.append(search_coord)
                    this_area.add(search_coord)
                    del garden[search_coord]

    total = 0
    for area in areas:
        # Fences are defined by the side of the grid coordiate they're on.
        # e.g. (1, 1, E) is a fence on the right of 1,1
        # This is useful if we have a case like below where the middle As shouldn't
        # Have their fences connect accross the middle.
        # So fence (2, 2, S) and (4, 4, N) won't end up connecting.
        # AAAAAA
        # AAABBA
        # AAABBA
        # ABBAAA
        # ABBAAA
        # AAAAAA
        fences = []
        for (x, y) in area:
            for ord, (dx, dy) in VECS.items():
                if (x+dx, y+dy) not in area:
                    fences.append((x, y, ord))

        def sortkey(fence):
            x, y, ord = fence
            if ord in ("E", "W"):
                return ord, x, y
            else: # ord in ("N", "S")
                return ord, y, x
        fences.sort(key=sortkey)
        sides = 0
        lx, ly, lord = (None, None, None)
        for x, y, ord in fences:
            ord_matches = lord == ord
            EW_match =  (
                (ord in ("E", "W"))
                and (lx == x)
                and (y - ly == 1)
            )
            NS_match = (
                (ord in ("N", "S"))
                and (ly == y)
                and (x - lx == 1)
            )
            if not (
                ord_matches
                and (EW_match or NS_match)
            ):
                sides += 1
            lx, ly, lord = x, y, ord

        total += sides * len(area)

    print(total)


if __name__ == "__main__":
    main()