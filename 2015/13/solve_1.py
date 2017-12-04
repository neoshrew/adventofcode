from itertools import permutations, tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


directed = {}
#Carol would lose 46 happiness units by sitting next to Eric.
#Carol would gain 33 happiness units by sitting next to Frank.
fname = 'input.txt'
#fname = 'input_test.txt'
with open(fname) as fandle:
    for line in fandle:
        parts = line.split()
        # Strip the trailing . in here.
        directed[(parts[0], parts[-1][:-1])] = \
            int(parts[3]) * (1 if parts[2] == 'gain' else -1)

names = set(k[0] for k in directed)

undirected = {}
for person_1 in names:
    for person_2 in names:
        if person_1 == person_2:
            continue

        undirected[(person_1, person_2)] = \
            directed[person_1, person_2] + directed[person_2, person_1]


max_score = None
# This will produce duplicates
for perm in permutations(names):
    this_score = undirected[perm[0], perm[-1]]

    for pair in pairwise(perm):
        this_score += undirected[pair]

    if this_score > max_score:
        max_score = this_score

print max_score