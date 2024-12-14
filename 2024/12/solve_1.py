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

VECS = [
    (-1, 0), # left
    (0, -1), # up
    (1, 0), # right
    (0, 1), # down
]
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
            for dx, dy in VECS:
                search_coord = (x+dx, y+dy)
                if garden.get(search_coord) == plant_type:
                    searching.append(search_coord)
                    this_area.add(search_coord)
                    del garden[search_coord]

    total = 0
    for area in areas:
        area_borders = 0
        for (x, y) in area:
            for dx, dy in VECS:
                if (x+dx, y+dy) not in area:
                    area_borders += 1
        total += len(area) * area_borders


    print(total)


if __name__ == "__main__":
    main()