import re

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

def get_input():
    stack_lines = []
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            line = line.rstrip()
            if '[' not in line:
                break
            stack_lines.append(line)

        n_rows = len(line.replace(' ', ''))

        stacks = [[] for i in range(n_rows)]

        for stack_line in stack_lines[::-1]:
            # "[Z] [M] [P]"
            # range(1, len(stack_line), 4)
            # start=1 because of the leading [
            # step=4 because each section of the pattern is 4 characters long
            #              e.g. "A] ["
            boxes_in_row = (stack_line[i] for i in range(1, len(stack_line), 4))
            for column, box_label in enumerate(boxes_in_row):
                if box_label == " ":
                    continue
                stacks[column].append(box_label)

        # move 1 from 2 to 1
        instr_re = re.compile("^move (\d+) from (\d+) to (\d+)")
        instructions = []
        for line in fandle:
            m = instr_re.match(line)
            if not m:
                continue
            instructions.append(tuple(int(i) for i in m.groups()))

    return stacks, instructions

def print_stacks(stacks):
    rows = max(len(i) for i in stacks)
    for row in range(rows-1, -1, -1):
        for stack in stacks:
            if len(stack) <= row:
                print("    ", end="")
            else:
                print("[{}] ".format(stack[row]), end="")
        print()

    print(" ".join(" {} ".format(i) for i in range(1,len(stacks)+1)))

def main():
    stacks, instructions = get_input()

    for move, from_, to in instructions:
        # Litter in the -1s 'cause the exercise isn't 0-indexed
        # Also there must be a way to do [-move:][::-1] in one slice,
        # but I cba figuring it out now.
        stacks[to-1].extend(stacks[from_-1][-move:][::-1])
        del stacks[from_-1][-move:]

    tops = ""
    for stack in stacks:
        if stack:
            tops += stack[-1]
    print(tops)


if __name__ == "__main__":
    main()
