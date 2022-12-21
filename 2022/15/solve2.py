import re

INPUT_FNAME, MIN, MAX = "input.txt", 0, 4000000
# INPUT_FNAME, MIN, MAX = "test_1.txt", 0, 20


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

def combine_ranges(ranges):
    ranges = sorted(ranges)
    i = 1
    while i < len(ranges):
        if ranges[i][0] <= ranges[i-1][1]+1:
            _, end = ranges.pop(i)
            ranges[i-1] = (ranges[i-1][0], max(ranges[i-1][1], end))
            
        else:
            i += 1
    return ranges
        
def main():
    sensors = get_sensors()

    for ROW in range(MIN, MAX):
        ranges = []
        for sensor, beacon in sensors.items():
            mdist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            rowdist = abs(sensor[1] - ROW)
            if rowdist <= mdist:        
                remainder = mdist-rowdist
                range_ = (
                    max(MIN, sensor[0]-remainder),
                    min(MAX, sensor[0]+remainder)
                )
                if range_[0] <= range_[1]:
                    ranges.append(range_)

        combined_ranges = combine_ranges(ranges)
        # There should be only one point, so only one row with two ranges
        if len(combined_ranges) > 1:
            y = ROW
            x = combined_ranges[0][1]+1
            break

    print(x*4000000+y)
    # This ended up taking a while to run, but oh well - onwards!
    #   $time python3 solve2.py
    #   11016575214126
    #
    #   real    0m25.249s
    #   user    0m25.249s
    #   sys     0m0.000s


if __name__ == "__main__":
    main()