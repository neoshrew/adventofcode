INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"
# INPUT_FNAME = "test_2.txt"

ROPE_LEN = 10

def get_instructions():
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            dir_raw, n_raw = line.strip().split()
            for _ in range(int(n_raw)):
                yield {
                    "R": (1, 0),
                    "U": (0, -1),
                    "L": (-1, 0),
                    "D": (0, 1),
                }[dir_raw]
            yield None, line.strip()

DIRECTIONS = [
    (dx, dy)
    for dx in range(-1, 2)
    for dy in range(-1, 2)
    if not (dx == dy == 0)
]
def get_move_to(chunk_a, chunk_b):
    if not (
        abs(chunk_a[0]-chunk_b[0]) > 1
        or abs(chunk_a[1]-chunk_b[1]) > 1
    ):
        # within 1, so don't move.
        return None

    # There's likely a more efficient way of doing this, but I'm lazy.
    # Just check which of the 8 different directions would bring us closest.
    # return that.
    return sorted(
        (abs(chunk_a[0]-(chunk_b[0]+dx))+abs(chunk_a[1]-(chunk_b[1]+dy)), (dx, dy))
        for dx, dy in DIRECTIONS
    )[0][1]

def print_ropestates(states, tail_visited):
    max_width = min_width = max_height = min_height = 0
    for _, rope_state in states:
        for x, y in rope_state:
            max_width = max(x, max_width)
            min_width = min(x, min_width)
            max_height = max(y, max_height)
            min_height = min(y, min_height)

    s = 0, 0

    for instr, rope_state in states:
        print(instr)
        cell_map = {s: 's'}
        cell_map.update({
            coord: i
            for i, coord in list(enumerate(rope_state))[::-1]
        })
        cell_map[rope_state[0]] = "H"
        for y in range(min_height, max_height+1):
            for x in range(min_width, max_width+1):
                print(cell_map.get((x, y), "."), end="")
            print()
        print()

    for y in range(min_height, max_height+1):
        for x in range(min_width, max_width+1):
            if (x, y) == s:
                print("s", end="")
            elif (x, y) in tail_visited:
                print("#", end="")
            else:
                print(".", end="")
        print()



def main():
    rope = [(0, 0)] * ROPE_LEN
    tail_visited = set([rope[-1]])

    states = []

    for instr in get_instructions():
        if instr[0] is None:
            states.append((instr[1], rope[::]))
            continue

        ix, iy = instr
        rope[0] = rope[0][0]+ix, rope[0][1]+iy
        for next_chunk in range(1, len(rope)):
            moveto = get_move_to(rope[next_chunk-1], rope[next_chunk])
            if not moveto:
                break
            dx, dy = moveto
            chunkx, chunky = rope[next_chunk]
            rope[next_chunk] = chunkx+dx, chunky+dy

        tail_visited.add(rope[-1])

    # print_ropestates(states, tail_visited)
    print(len(tail_visited))

if __name__ == "__main__":
    main()
