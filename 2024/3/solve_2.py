import re

FNAME = "input.txt"
# FNAME = "test2.txt"


def main():
    with open(FNAME) as fandle:
        raw_program = fandle.read()

    valid_instructions = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", raw_program)

    def mul_from_str(mul_str):
        a, b = [int(i) for i in mul_str[4:-1].split(',')]
        return a*b

    total = 0
    active = True
    for instr in valid_instructions:
        if instr == "do()":
            active = True
        elif instr == "don't()":
            active = False
        elif active:
            total += mul_from_str(instr)

    print(total)

if __name__ == "__main__":
    main()