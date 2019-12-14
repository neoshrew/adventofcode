from itertools import count
from collections import defaultdict
import re

fname = "input.txt"
# fname = "test_1.txt"
with open(fname) as fandle:
    MOONS = [
        [int(i) for i in match]
        for match in (
            re.findall("-?[0-9]+", line)
            for line in fandle
        )
        if match
    ]


def set_step(points, velocities):
    for a, point_a in enumerate(points):
        for b, point_b in enumerate(points[a+1:], a+1):
            if point_a < point_b:
                velocities[a] += 1
                velocities[b] -= 1
            elif point_a > point_b:
                velocities[a] -= 1
                velocities[b] += 1

    for i, velocity in enumerate(velocities):
        points[i] += velocity


def resolve_set(points):
    velocities = [0]*len(points)
    def frz():
        return (tuple(points), tuple(velocities))
    first = frz()

    for i in count(1):
        set_step(points, velocities)
        if first == frz():
            return i

# Lazily stolen from
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = defaultdict(int)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors

# gcm - greatest common multiple
gcm_factors = {}
for axis_positions in zip(*MOONS):
    len_period = resolve_set(list(axis_positions))
    pfs = prime_factors(len_period)
    for f, c in pfs.items():
        gcm_factors[f] = max(c, gcm_factors.get(f, c))

total = 1
for f, c in gcm_factors.items():
    total *= f**c

print(total)
