fname = "input.txt"
# fname = "test_input1.txt"

posx, posy = 0, 0
unit_vectors = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}
dirs = ['N', 'E', 'S', 'W']
facing = 1

with open(fname) as fandle:
    for line in fandle:
        action, magnitude = line[0], int(line[1:])

        if action == 'F':
            action = dirs[facing]

        if action in unit_vectors:
            dx, dy = unit_vectors[action]
            posx += dx * magnitude
            posy += dy * magnitude

        elif action in ('L', 'R'):
            divisor = 90 if action == 'R' else -90
            magnitude //= divisor
            facing += magnitude
            facing %= 4

        else:
            raise Exception(f"wat {action}")

print (abs(posx) + abs(posy))
