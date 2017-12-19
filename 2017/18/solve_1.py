from collections import defaultdict

instructions = []

with open('input.txt') as fandle:
    for line in fandle:
        parts = line.split()

        cmd = parts[0]
        operand1 = parts[1]

        try:
            operand2 = int(parts[2])
        except ValueError:
            operand2 = parts[2]
        except IndexError:
            operand2 = None

        try:
            operand1 = int(parts[1])
        except ValueError:
            operand1 = parts[1]
        except IndexError:
            operand1 = None

        instructions.append((cmd, operand1, operand2))

registers = defaultdict(int)
sound = None

index = 0
while 0 <= index < len(instructions):
    cmd, op1, op2 = instructions[index]

    if isinstance(op2, str):
        op2_val = registers[op2]
    else:
        op2_val = op2

    if isinstance(op1, str):
        op1_val = registers[op1]
    else:
        op1_val = op1

    if cmd == 'snd':
        sound = op1_val

    elif cmd == 'set':
        registers[op1] = op2_val

    elif cmd == 'add':
        registers[op1] += op2_val

    elif cmd == 'mul':
        registers[op1] *= op2_val

    elif cmd == 'mod':
        registers[op1] %= op2_val

    elif cmd == 'rcv':
        if op1_val != 0:
            break

    if cmd == 'jgz' and op1_val > 0:
        index += op2_val

    else:
        index += 1

print sound