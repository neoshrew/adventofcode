from functools import reduce

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
    # doing a lazy chunker
    with open(INPUT_FNAME) as fandle:
        all_lines = [line.strip() for line in fandle]

    triples = (
        [set(triple) for triple in all_lines[i:i+3]]
        for i in range(0, len(all_lines), 3)
    )

    total = 0
    for triple in triples:
        common = reduce((lambda x, y: x&y), triple).pop()
        total += priorities[common]

    print(total)


if __name__ == "__main__":
    main()
