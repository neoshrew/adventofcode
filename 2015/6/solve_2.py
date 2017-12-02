def on(x):
    return x+1

def off(x):
    return 0 if x==0 else x-1

def toggle(x):
    return x+2

opdict = {'on':on, 'off': off}

def parscoord(x):
    i, j = x.split(',')
    return (int(i), int(j))

instructions = []
with open('input.txt') as fandle:
#    fandle = [
#        'toggle 0,0 _ 9,9',
#        'toggle 0,0 _ 3,3',
#        'turn on 2,2 _ 3,3',
#        'turn off 8,0 _ 9,8',
#    ]
#
    for raw in fandle:
        split = raw.split()
        if split[0] == 'toggle':
            instructions.append(
                (toggle, parscoord(split[1]), parscoord(split[3]))
            )
        else:
            instructions.append(
                (opdict[split[1]], parscoord(split[2]), parscoord(split[4]))
            )


gridsize = 1000
grid = [[0 for _ in range(gridsize)] for _ in range(gridsize)]

for op, (start_x, start_y), (end_x, end_y) in instructions:
    if start_x > end_x:
        start_x, end_x = end_x, start_x
    if start_y > end_y:
        start_y, end_y = end_y, start_y

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            grid[x][y] = op(grid[x][y])

#print '\n'.join(row for row in (''.join(str(cell) for cell in row) for row in grid))

print sum(sum(i) for i in grid)