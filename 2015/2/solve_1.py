from itertools import combinations

total = 0

with open('input.txt') as fandle:
    for raw_row in fandle:
        raw_row = raw_row.strip()
        row = tuple(int(i) for i in raw_row.split('x'))

        sides = [i*j for i, j in combinations(row, 2)]

        total += min(sides) + (sum(sides)*2)

print total