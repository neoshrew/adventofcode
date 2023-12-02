FNAME = "input.txt"
# FNAME = "test2.txt"

NUMBER_MAP = {
    s: str(i)
    for i, s in enumerate(
        ("one","two","three","four","five","six","seven","eight","nine"),
        start=1
    )
}
ALL_DIGITS = list(NUMBER_MAP.keys()) + list(NUMBER_MAP.values())

def get_input():
    with open(FNAME) as fandle:
        for line in fandle:
            if line:
                yield line.strip()

def str_find_all(string, pattern):
    curr = 0
    while True:
        curr = string.find(pattern, curr)
        if curr == -1:
            break
        yield curr
        curr += 1


def solve():
    total = 0
    for line in get_input():
        # eightwothree
        # This is from the example - so characters can be re-used for
        # different numbers. So we can't just do a dumb replace.

        digit_locs = {
            loc: NUMBER_MAP.get(digit_string, digit_string)
            for digit_string in ALL_DIGITS
            for loc in str_find_all(line, digit_string)
        }
        digits = [loc for _, loc in sorted(digit_locs.items())]
        these_digits = digits[0]+digits[-1]
        total += int(these_digits)
    print(total)


if __name__ == "__main__":
    solve()