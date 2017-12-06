from itertools import count

with open('input.txt') as fandle:
    banks = [int(i) for i in fandle.read().split()]

seen = dict()
seen[tuple(banks)] = 0

for total_cycles in count(1):
    index = banks.index(max(banks))
    remaining_blocks = banks[index]
    banks[index] = 0
    index += 1

    while remaining_blocks:
        if index == len(banks):
            index = 0

        banks[index] += 1
        index += 1
        remaining_blocks -= 1

    tup = tuple(banks)
    if tup in seen:
        break

    seen[tup] = total_cycles

print len(seen) - seen[tup]