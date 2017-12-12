edges = {}

with open('input.txt') as fandle:
    for line in fandle:
        n, others = line.strip().split(' <-> ')
        n = int(n)
        edges[n] = [int(i) for i in others.split(', ')]


group = set()
to_check = [0]
while to_check:
    n = to_check.pop()
    group.add(n)
    to_check.extend(
        i
        for i in edges[n]
        if i not in group
    )

print len(group)
