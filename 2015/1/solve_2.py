from itertools import count

with open('input.txt') as fandle:
    data = fandle.read().strip()

total = 0
for i, x in enumerate(data, 1):
    total += 1 if x == '(' else -1
    if total < 0:
        print i
        break