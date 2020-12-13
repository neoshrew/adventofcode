fname = "input.txt"
# fname = "test_input1.txt"


with open(fname) as fandle:
    program = [
        (instruction, int(operand))
        for instruction, operand in (
            line.rstrip().split()
            for line in fandle
        )
    ]

acc = pc = 0
visited = set()
while pc not in visited:
    instruction, operand = program[pc]
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

print(acc)
