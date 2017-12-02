from itertools import permutations, tee, izip

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

distances = {}

with open('input.txt') as fandle:
    for line in fandle:
        split = line.split()
        distances[(split[0], split[2])] = int(split[4])

for endpoints, distance in distances.items():
    distances[endpoints[::-1]] = distance
locations = set(loc[0] for loc in distances.keys())

routes = []

for route in permutations(locations):
    route_distance = sum(
        distances[tuple(sorted(pair))]
        for pair in pairwise(route)
    )
    routes.append(route_distance)

print max(routes)