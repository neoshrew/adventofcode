from operator import mul
from functools import reduce
from itertools import combinations

with open("input.txt") as fandle:
    package_weights = [
        int(line)
        for line in fandle
        if line.strip()
    ]

# package_weights = [1,2,3,4,5,7,8,9,10,11]

compartments = 3
split = sum(package_weights)//compartments

# Dumb brute force to find smallest number of packages
# for the passenger comparment
def weights_getter():
    will_break = False
    for i in range(len(package_weights)//compartments+1):
        for j in combinations(package_weights, i):
            if sum(j) == split:
                yield j
                will_break = True

        if will_break:
            break

quantum_engtanglement = min(
    reduce(mul, possibility)
    for possibility in weights_getter()
)

print(quantum_engtanglement)
