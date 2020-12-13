from copy import deepcopy

fname = "input.txt"
# fname = "test_input1.txt"

OCCUPIED = "#"
SEAT = "L"
FLOOR = "."

SEATS = {}
with open(fname) as fandle:
    for x, line in enumerate(fandle):
        line = line.rstrip()
        for y, cell in enumerate(line):
            if cell == SEAT:
                SEATS[(x, y)] = [SEAT, []]

DIMS = x+1, y+1
def in_grid(x, y):
    global DIMS
    return (
        0 <= x <= DIMS[0]
        and 0 <= y <= DIMS[1]
    )

vectors = tuple(
    (dx, dy)
    for dx in range(-1, 2)
    for dy in range(-1, 2)
    if dx != 0 or dy != 0
)

for (seatx, seaty), (_, can_see) in SEATS.items():
    for dx, dy in vectors:
        x, y = seatx, seaty
        while True:
            x, y = x+dx, y+dy
            if not in_grid(x, y):
                break
            if (x, y) in SEATS:
                can_see.append((x, y))
                break

def get_can_see_count(coords):
    global SEATS
    return sum(
        1 if SEATS[can_see][0] == OCCUPIED else 0
        for can_see in SEATS[coords][1]
    )


to_change = [None]
while to_change:
    to_change.clear()
    for coords, (state, can_see) in SEATS.items():
        sc = get_can_see_count(coords)
        if state == SEAT and sc == 0:
            to_change.append(coords)
        elif state == OCCUPIED and sc >= 5:
            to_change.append(coords)

    for i in to_change:
        deets = SEATS[i]
        deets[0] = OCCUPIED if deets[0] == SEAT else SEAT

print(sum(
    1 if state == OCCUPIED else 0
    for state, _ in SEATS.values()
))
