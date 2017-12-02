with open('input.txt') as fandle:
    data = fandle.read()

vectors = [
    ({'<':-1, '>':1}.get(i, 0), {'^':-1, 'v':1}.get(i, 0))
    for i in data.strip()
]

current_location = (0, 0)
locations = {current_location}
for vector in vectors:
    current_location = (
        current_location[0] + vector[0],
        current_location[1] + vector[1],
    )
    locations.add(current_location)

print len(locations)