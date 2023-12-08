import re
from collections import defaultdict

FNAME = "input.txt"
# FNAME = "test3.txt"


# AAA = (BBB, BBB)
ROUTE_RE = re.compile("^([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)$")
def get_map_data():
    with open(FNAME) as fandle:
        instrictions = fandle.readline().strip()
        fandle.readline()
        grid = {}
        for line in fandle:
            match = ROUTE_RE.match(line)
            if not match:
                continue
            start, left, right = match.groups()
            grid[start] = left, right

    return instrictions, grid


def get_prime_factors(n):
    assert n > 1
    # Just divide by all the numbers. If you wanted to optimize this,
    # you could use a prime sieve to only give you prime numbers.
    i = 2
    factors = defaultdict(int)
    while n > 1:
        if n % i == 0:
            factors[i] += 1
            n//=i
        else:
            i += 1
    return dict(factors)


def main():
    instructions, grid = get_map_data()

    # Modelling all of the paths at once to see when they converge could take
    # a _loooong_ time. So instead run each path, get its length, and then
    # find the lowest common multiple which will be the first time
    # all of the cycles match up.

    factors = {}
    starting_paths = (
        pos
        for pos in grid
        if pos.endswith("A")
    )
    for curr_pos in starting_paths:
        steps = 0
        while not curr_pos.endswith("Z"):
            l_or_r = instructions[steps % len(instructions)]
            curr_pos = grid[curr_pos][{"L": 0, "R": 1}[l_or_r]]
            steps += 1

        for factor, count in get_prime_factors(steps).items():
            if factors.get(factor, 0) < count:
                factors[factor] = count

    total = 1
    for factor, count in factors.items():
        total *= factor * count

    print(total)

if __name__  == "__main__":
    main()
