INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6
SPRITE_WIDTH = 3
SPRITE_RADIUS = SPRITE_WIDTH // 2

def get_instructions():
    with open(INPUT_FNAME) as fandle:
        for line_raw in fandle:
            line = line_raw.strip().split()
            if line[0] == "noop":
                yield ("noop", None)
            elif line[0] == "addx":
                yield ("addx", int(line[1]))
            else:
                raise Exception("wat")

def get_silly_noop_injection_instructions():
    for instr in get_instructions():
        if instr[0] == "addx":
            yield ("noop", None)
        yield instr

def main():
    screen = []
    X = 1
    instructions = get_silly_noop_injection_instructions()
    for cycle, (op, operand) in enumerate(instructions, 1):
        # cycle -1 'cause the screen is 0-indexed, but the
        # CPU cycles aren't.
        if X-SPRITE_RADIUS <= (cycle-1) % SCREEN_WIDTH <= X+SPRITE_RADIUS:
            screen.append('#')
        else:
            screen.append('.')

        if op == "addx":
            X += operand

    for y in range(SCREEN_HEIGHT):
        print("".join(screen[SCREEN_WIDTH*y:SCREEN_WIDTH*(y+1)]))

if __name__ == "__main__":
    main()
