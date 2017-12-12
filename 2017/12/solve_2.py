edges = {}

with open('input.txt') as fandle:
    for line in fandle:
        n, others = line.strip().split(' <-> ')
        n = int(n)
        edges[n] = [int(i) for i in others.split(', ')]


all_ids = set(edges)
groups = []

while all_ids:
    this_group = set()
    to_check = [all_ids.pop()]
    while to_check:
        n = to_check.pop()
        all_ids.discard(n)
        this_group.add(n)
        to_check.extend(
            i
            for i in edges[n]
            if i in all_ids
        )
    groups.append(this_group)

print len(groups)
