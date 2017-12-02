with open('input.txt') as fandle:
    data = fandle.read()

vectors = [
    ({'<':-1, '>':1}.get(i, 0), {'^':-1, 'v':1}.get(i, 0))
    for i in data.strip()
]

working_location = other_location = (0, 0)
locations = {working_location}
for vector in vectors:
    current_location = (
        working_location[0] + vector[0],
        working_location[1] + vector[1],
    )
    locations.add(current_location)

    working_location = other_location
    other_location = current_location

print len(locations)