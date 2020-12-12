# 2-9 c: ccccccccc
# 1-3 b: cdefg
# 1-3 a: abcde

import re

RE = re.compile("^(\d+)-(\d+) +([a-z]): (.*)$")

fname = "input.txt"
# fname = "test_input1.txt"

total = 0
with open(fname) as fandle:
    for line in fandle:
        match = RE.match(line)
        if not match:
            continue

        first_pos, second_pos, char, password = match.groups()
        first_pos, second_pos = int(first_pos), int(second_pos)

        firstmatch = password[first_pos-1] == char
        secondmatch = password[second_pos-1] == char

        if firstmatch ^ secondmatch:
            total += 1

print(total)
