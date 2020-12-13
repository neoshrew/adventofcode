fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input1_halting.txt"


with open(fname) as fandle:
    program = [
        (instruction, int(operand))
        for instruction, operand in (
            line.rstrip().split()
            for line in fandle
        )
    ]


def run_program(program):
    acc = pc = 0
    visited = set()
    while pc not in visited:
        try:
            instruction, operand = program[pc]
        except IndexError:
            return True, acc, None

        visited.add(pc)
        pc_mod = 1

        if instruction == "acc":
            acc += operand
        elif instruction == "jmp":
            pc_mod = operand
        elif instruction == "nop":
            pass
        else:
            print("got unknown instruction", instruction)

        pc += pc_mod

    return False, acc, visited

# Only an instruction we currently visit will have an effect if we change it
# so run the current infinite program once and check what instructions
# are currently executed.
*_, visited = run_program(program)

# the last good instruction we can jump to to halt.
# this is at least out of bounds, but work backwards
# from this to find the last "jmp" which would bring us back before it.
for i in range(len(program)-1, 0, -1):
    if program[i][0] != "jmp":
        continue
    if program[i][1] <= 0:
        last_good_instruction = i+1
        break

candidates = set(
    i
    for i in visited
    if i < last_good_instruction
    and program[i][0] in ("jmp", "nop")
    and program[i] != ("nop", 0)
)

for candidate in candidates:
    cmd, operand = program[candidate]
    program[candidate] = ("nop" if cmd == "jmp" else "jmp", operand)
    ends, acc, _ = run_program(program)
    if ends:
        break
    program[candidate] = (cmd, operand)

print(acc)
