INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

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

def need_move_tail(head, tail):
    return (abs(head[0]-tail[0]) > 1) | (abs(head[1]-tail[1]) > 1)

def main():
    head = tail = (0, 0)
    tail_visited = set([tail])
    for dx, dy in get_instructions():
        h_last = head
        head = head[0]+dx, head[1]+dy
        if need_move_tail(head, tail):
            # The trick here is that, even thought the instructions are
            # convoluted, no matter how the tail is dragged it just ends up
            # where the head last was (if it needs dragging)
            tail = h_last
            tail_visited.add(tail)
    print(len(tail_visited))

if __name__ == "__main__":
    main()
