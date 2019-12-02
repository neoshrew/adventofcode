

with open('input.txt') as fandle:
    command_line = fandle.readline()

program = {}
for pos, opcode_raw in enumerate(command_line.strip().split(',')):
    opcode = int(opcode_raw)
    program[pos] = opcode


# Make our adjustments
# replace position 1 with the value 12 and replace position 2 with the value 2.
program[1] = 12
program[2] = 2

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

print(program[0])
