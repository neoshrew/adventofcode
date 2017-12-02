from itertools import tee, izip

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return (''.join(i) for i in izip(a, b))

def pairwise_gap(iterable):
    a, b = tee(iterable)
    next(b, None)
    next(b, None)
    return (''.join(i) for i in izip(a, b))

fname = 'test_input_2.txt'
fname = 'input.txt'
with open(fname) as fandle:
    names = [i.strip() for i in fandle if i.strip()]


vowels = 'aeiou'
bad_strings = {'ab', 'cd', 'pq', 'xy'}

total = 0
for name in names:
    # Must have a repeating, but non-overlapping character pair pair
    found = False
    for i, x in enumerate(pairwise(name), 2):
        for y in pairwise(name[i:]):
            if x == y:
                break
        else:
            continue
        break
    else:
        continue

    # must have a repeated character with a character in the middle
    for pair in pairwise_gap(name):
        if pair[0] == pair[1]:
            break
    else:
        continue

    total += 1

print total