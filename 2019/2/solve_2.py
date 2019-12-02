

with open('input.txt') as fandle:
    command_line = fandle.readline()

program = {}
for pos, opcode_raw in enumerate(command_line.strip().split(',')):
    opcode = int(opcode_raw)
    program[pos] = opcode


def calculate_program(program):
    pos = -4
    while True:
        pos += 4
        op = program[pos]

        if op == 99:
            break

        operand_1 = program[program[pos+1]]
        operand_2 = program[program[pos+2]]
        dest = program[pos+3]

        if op == 1:
            program[dest] = operand_1 + operand_2
        else: # op == 2
            program[dest] = operand_1 * operand_2

    return program[0]

target = 19690720
for i in range(0, 99):
    for j in range(0, 99):
        new_program = {**program}
        new_program[1] = i
        new_program[2] = j
        if calculate_program(new_program) == target:
            print(100*i + j)
            break
