from operator import add, mul

FNAME = "input.txt"
# FNAME = "test1.txt"


def get_tests():
    tests = []
    with open(FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if not line:
                continue

            raw_result, raw_values = line.split(": ")
            tests.append((
                int(raw_result),
                [int(i) for i in raw_values.split(" ")],
            ))

    return tests

def concat(a, b):
    return int(str(a)+str(b))
OPS = (add, mul, concat)
def possible_values(values):
    if len(values) == 1:
        return {values[0]}

    this_val = values[-1]
    values = values[:-1]

    retvals = set()
    for op in OPS:
        for value in possible_values(values):
            retvals.add(op(value, this_val))

    return retvals


def main():
    tests = get_tests()    

    total = 0

    for result, inputs in tests:
        pvs = possible_values(inputs)
        if result in pvs:
            total += result

    print(total)

if __name__ == "__main__":
    main()