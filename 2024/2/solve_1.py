FNAME = "input.txt"
# FNAME = "test1.txt"

def get_reports():
    with open(FNAME) as fandle:
        return [
            [int(level) for level in line.split()]
            for line in fandle
        ]


def sign(i):
    if i < 0:
        return -1
    if i > 0:
        return 1
    return 0


def main():
    reports = get_reports()

    total = 0
    for report in reports:
        gaps = [
            report[i+1] - report[i]
            for i in range(len(report)-1)
        ]
        if (
            all((1 <= abs(gap) <= 3) for gap in gaps)
            and len(set(sign(gap) for gap in gaps)) == 1
        ):
            total += 1

    print(total)

if __name__ == "__main__":
    main()