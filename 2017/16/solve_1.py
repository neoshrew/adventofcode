with open('input.txt') as fandle:
    raw_commands = fandle.read().strip().split(',')


positions = [chr(i) for i in range(ord('a'), ord('p')+1)]


for command in raw_commands:
    #print ''.join(positions), '->',
    cmd, rest = command[0], command[1:]

    if cmd == 's':
        fac = int(rest)
        positions[::] = positions[-fac:] + positions[:-fac]

    elif cmd == 'x':
        split = rest.split('/')
        pos1 = int(split[0])
        pos2 = int(split[1])
        positions[pos1], positions[pos2] = positions[pos2], positions[pos1]

    elif cmd == 'p':
        split = rest.split('/')
        pos1 = positions.index(split[0])
        pos2 = positions.index(split[1])
        positions[pos1], positions[pos2] = positions[pos2], positions[pos1]

    else:
        raise Exception("bad command "+command)

    #print ''.join(positions)

print ''.join(positions)

