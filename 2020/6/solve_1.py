fname = "input.txt"

total = 0
with open(fname) as fandle:
    curr = set()
    for line in fandle:
        line = line.rstrip()
        if not line:
            total += len(curr)
            curr = set()
        curr |= set(line)
    if curr:
        total += len(curr)

print(total)
