from collections import Counter

fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input2.txt"

with open(fname) as fandle:
    adapters = sorted(int(line) for line in fandle)

adapters.insert(0, 0)
adapters.append(adapters[-1]+3)

counts = Counter(
    adapters[i+1]-adapters[i]
    for i in range(len(adapters)-1)
)

print(counts[1]*counts[3])
