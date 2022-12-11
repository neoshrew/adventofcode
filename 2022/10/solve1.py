INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

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
    interested_in = set([20, 60, 100, 140, 180, 220])
    total = 0
    X = 1
    instructions = get_silly_noop_injection_instructions()
    for cycle, (op, operand) in enumerate(instructions, 1):
        # We care about "during", addx finished at the end
        if cycle in interested_in:
            total += cycle*X
        if op == "addx":
            X += operand

    print(total)

if __name__ == "__main__":
    main()
