from collections import Counter

fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input2.txt"

with open(fname) as fandle:
    # in theory you could have duplicate adapters
    # however I've checked my input and tests, and there
    # are none
    adapters = set(int(line) for line in fandle)

target = max(adapters)

cache = {}
def get_possibilities(curr):
    if curr == target:
        return 1

    if curr in cache:
        return cache[curr]

    result = sum(
        get_possibilities(curr+i)
        for i in range(1, 4)
        if curr+i in adapters
    )
    cache[curr] = result
    return result

print(get_possibilities(0))
