FNAME = "input.txt"
# FNAME = "test1.txt"


def get_input():
    with open(FNAME) as fandle:
        for line in fandle:
            if line:
                yield line.strip()

def solve():
    total = 0
    for line in get_input():
        digits = [c for c in line if c.isdigit()]

        total += int(digits[0]+digits[-1])
    print(total)


if __name__ == "__main__":
    solve()