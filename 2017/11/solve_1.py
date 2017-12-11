with open('input.txt') as fandle:
    moves = fandle.read().strip().split(',')

vectors = {
    'n':  ( 0, -2),
    's':  ( 0,  2),
    'ne': ( 1, -1),
    'nw': (-1, -1),
    'se': ( 1,  1),
    'sw': (-1,  1),
}


def solve(moves):
    total = [0, 0]
    for move in moves:
        vec = vectors[move]
        total[0] += vec[0]
        total[1] += vec[1]

    # y can be traversed twice as fast,
    # so take off the steps which can be done at
    # twice the speed
    total[1] = (total[1] // 2) + (total[1] % 2)

    return max(total)


#print solve(['ne', 'ne', 'ne'])
#print solve(['ne', 'ne', 'sw', 'sw'])
#print solve(['ne', 'ne', 's', 's'])
#print solve(['se', 'sw', 'se', 'sw', 'sw'])
print solve(moves)
