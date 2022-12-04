import re

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

_LINE_RE = re.compile("^(\d+)-(\d+),(\d+)-(\d+)$")
def get_pairings():
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            # 93-94,34-93
            ns = list(map(int, _LINE_RE.match(line).groups()))
            yield ((ns[0], ns[1]), (ns[2], ns[3]))

def main():
    total = 0

    # I could do a faster start/end range comparison.
    # I could not use loads of memory for no reason.
    # but I'm lazy.
    for elf1, elfA in get_pairings():
        elf1 = set(range(elf1[0], elf1[1]+1))
        elfA = set(range(elfA[0], elfA[1]+1))
        if elf1.issubset(elfA) or elfA.issubset(elf1):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
