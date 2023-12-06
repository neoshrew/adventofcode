import math

FNAME = "input.txt"
# FNAME = "test1.txt"

def main():
    # Time:      7  15   30
    # Distance:  9  40  200
    def parseline(line):
        return int(line.split(" ", 1)[1].replace(" ", ""))

    with open(FNAME) as fandle:
        race_time = parseline(fandle.readline())
        record = parseline(fandle.readline())

    # I freakin' knew it.
    # quadratic formula time I guess.
    # time = hold_time * (race_time - hold_time)
    # time = -hold_time^2 + hold_time*race_time
    # we want it to match record_time + 1 (to beat it)
    # (we're also doing discrete maths here)
    # record+1 = -hold_time^2 + hold_time*race_time
    # to 0 for the quadratic formula
    # 0 = -hold_time^2 + hold_time*race_time - (record+1)
    # x = (-b ± sqrt(b^2 - 4ac))/(2a)
    # a = -1   b = race_time   c = -(record+1)
    discriminant = race_time**2 - 4*-1*-(record+1)
    dis_root = math.sqrt(discriminant)
    upper_solution = (-race_time-dis_root)/-2
    lower_solution = (-race_time+dis_root)/-2
    # upper will be higher, 'cause the numerator will be larger magnitude but
    # lower 'cause it's negative, but it's all over -2 so endsup higher

    # we're really supposed to be in the land of integers. So we want the
    # ceil of lower, 'cause the first integer solution is >= lower.
    # and the opposide for higher
    shortest_hold = math.ceil(lower_solution)
    longest_hold = math.floor(upper_solution)
    # we +1 here because our range is inclusive
    solutions = longest_hold - shortest_hold +1

    print(solutions)

if __name__ == "__main__":
    main()
