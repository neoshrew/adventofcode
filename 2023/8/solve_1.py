import re

FNAME = "input.txt"
# FNAME = "test1.txt"
# FNAME = "test2.txt"


# AAA = (BBB, BBB)
ROUTE_RE = re.compile("^([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)$")
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


def main():
    instructions, grid = get_map_data()

    steps = 0
    curr_pos = "AAA"
    while curr_pos != "ZZZ":
        l_or_r = instructions[steps % len(instructions)]
        curr_pos = grid[curr_pos][{"L": 0, "R": 1}[l_or_r]]
        steps += 1

    print(steps)

if __name__  == "__main__":
    main()
