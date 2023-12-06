FNAME = "input.txt"
# FNAME = "test1.txt"


def get_race_details():
    with open(FNAME) as fandle:
        # Time:      7  15   30
        # Distance:  9  40  200
        return list(zip(
            [int(i) for i in fandle.readline().split()[1:]],
            [int(i) for i in fandle.readline().split()[1:]],
        ))


def main():
    race_details = get_race_details()

    # 'cause we're multiplying
    total = 1
    # Part 1 feels tractable to do the brute force way.
    # So I'm going to do it that way.
    # And fully expect part two to be intractable and require some thinking
    for race_time, race_record in race_details:
        possible_hold_times = 0
        for hold_time in range(race_time+1):
            if hold_time * (race_time - hold_time) > race_record:
                possible_hold_times += 1
        if possible_hold_times:
            total *= possible_hold_times

    print(total)

if __name__ == "__main__":
    main()
