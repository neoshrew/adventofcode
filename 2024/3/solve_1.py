import re

FNAME = "input.txt"
# FNAME = "test1.txt"


def main():
    with open(FNAME) as fandle:
        raw_program = fandle.read()

    valid_muls = re.findall("mul\([0-9]+,[0-9]+\)", raw_program)

    def mul(a, b):
        return a*b

    total = sum(
        # slice off the 'mul(' and ')'
        mul(*[int(i) for i in mul_str[4:-1].split(',')])
        for mul_str in valid_muls
    )

    print(total)

if __name__ == "__main__":
    main()