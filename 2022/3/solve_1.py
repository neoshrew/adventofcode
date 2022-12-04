INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"


priorities = {
    char: priority
    for (priority, char) in enumerate (
        [chr(i) for i in range(ord("a"), ord("z")+1)] \
            + [chr(i) for i in range(ord("A"), ord("Z")+1)],
        1
    )

}
def main():
    total = 0

    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            pack_a = set(line[:len(line)//2])
            pack_b = set(line[len(line)//2:])
            similar = (pack_a & pack_b).pop()

            total += priorities[similar]
    print(total)


if __name__ == "__main__":
    main()
