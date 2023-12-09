FNAME = "input.txt"
# FNAME = "test1.txt"


def get_sequences():
    with open(FNAME) as fandle:
        for line in fandle:
            if line.strip():
                yield [int(i) for i in line.split()]


def get_next(seq):
    differences = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    if all(d == 0 for d in differences):
        return seq[0]

    return seq[0] - get_next(differences)


def main():
    total = 0
    for seq in get_sequences():
        total += get_next(seq)

    print(total)


if __name__ == "__main__":
    main()