fname = "input.txt"
# fname = "test_input1.txt"

total = 0
with open(fname) as fandle:
    curr = None
    for line in fandle:
        line = line.rstrip()
        if not line:
            total += len(curr)
            print("flush", len(curr), total, '\n')
            curr = None
            continue

        if curr is None:
            curr = set(line)
        else:
            curr &= set(line)

        print(line, len(curr), curr)

    if curr:
        total += len(curr)
        print("flush", len(curr), total, '\n')

print(total)
