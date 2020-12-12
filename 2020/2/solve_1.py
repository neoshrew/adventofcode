# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

import re

RE = re.compile("^(\d+)-(\d+) +([a-z]): (.*)$")

total = 0
with open("input.txt") as fandle:
    for line in fandle:
        match = RE.match(line)
        if not match:
            continue

        lim_min, lim_max, char, password = match.groups()
        lim_min, lim_max = int(lim_min), int(lim_max)

        if lim_min <= password.count(char) <= lim_max:
            total += 1

print(total)
