import re

INPUT_FNAME, ROW = "input.txt", 2000000
# INPUT_FNAME, ROW = "test_1.txt", 10


def get_sensors():
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    my_re = re.compile(
        "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    sensors = {}
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            match = my_re.match(line)
            coords = [int(i) for i in match.groups()]
            sensors[coords[0], coords[1]] = (coords[2], coords[3])

    return sensors

def main():
    sensors = get_sensors()

    filled_x_points = set(
        j[0]
        for i in sensors.items()
        for j in i
        if j[1] == ROW
    )

    points = set()
    for sensor, beacon in sensors.items():
        # for each sensor get the Manhattan distance to the nearest beacon
        mdist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        # get dist to the interested row
        rowdist = abs(sensor[1] - ROW)
        # check if that row is even within the Manhattan distance.
        if rowdist > mdist:
            continue
        # otherwise, the number of points on that row within the mdist is 1
        # (the point in the same column as our origin) plus twice the remainder
        # after the row dist.
        # But 'cause we might have multiple sensors with overlapping areas,
        # let's store all of those points.
        remainder = mdist-rowdist
        for x in range(sensor[0]-remainder, sensor[0]+remainder+1):
            # irritating that if a sensor/beacon is on this line that point
            # on the line _is not_ counted. But it's a position where the
            # distress beacon couldn't be!
            if x not in filled_x_points:
                points.add(x)

    print(len(points))


if __name__ == "__main__":
    main()