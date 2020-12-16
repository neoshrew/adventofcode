fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input2.txt"


unit_vectors = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}
shipx, shipy = 0, 0
wayx, wayy = 10, -1


with open(fname) as fandle:
    for line in fandle:
        action, magnitude = line[0], int(line[1:])

        if action == 'F':
            shipx += magnitude * wayx
            shipy += magnitude * wayy

        elif action in unit_vectors:
            dx, dy = unit_vectors[action]
            wayx += dx * magnitude
            wayy += dy * magnitude

        else: # action in ('L', 'R'):
            magnitude = (magnitude // 90) % 4
            if magnitude == 2: # 180
                wayx, wayy = -wayx, -wayy

            elif (action, magnitude) in (('L', 3), ('R', 1)):
                wayx, wayy = -wayy, wayx

            else: #(action, magnitude) in (('L', 1), ('R', 3)):
                wayx, wayy = wayy, -wayx

print (abs(shipx) + abs(shipy))
