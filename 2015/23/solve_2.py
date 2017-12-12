with open('input.txt') as fandle:
    instructions = [
        [part.replace(',', '') for part in line.split()]
        for line in fandle
    ]

registers = {'a': 1, 'b': 0}

i = 0
while 0 <= i < len(instructions):
    line = instructions[i]
    cmd = line[0]
    step = 1

    if cmd == 'hlf':
        registers[line[1]] /= 2

    elif cmd == 'tpl':
        registers[line[1]] *= 3

    elif cmd == 'inc':
        registers[line[1]] += 1

    elif cmd == 'jmp':
        step = int(line[1])

    elif cmd == 'jie' and (registers[line[1]] % 2 == 0):
        step = int(line[2])

    elif cmd == 'jio' and (registers[line[1]] == 1):
        step = int(line[2])

    i += step

print registers['b']
