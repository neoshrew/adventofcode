from operator import mul

total = 0

with open('input.txt') as fandle:
    for raw_row in fandle:
        raw_row = raw_row.strip()
        row = tuple(int(i) for i in raw_row.split('x'))

        total += reduce(mul, row) + (2*sum(sorted(row)[:2]))

print total