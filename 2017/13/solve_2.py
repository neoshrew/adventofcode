from itertools import count

fname = 'input.txt'
#fname = 'input_test.txt'

with open(fname) as fandle:
    levels = {
        int(k): int(v)
        for k, v in (
            line.split(': ')
            for line in fandle
        )
    }

# Eh, takes about 20s on my 4th gen i7.

def get_severity(delay):
    # each layer has a cycle of 2*(range-2) + 2
    # if that cycle is a factor of its level, then it will collide.

    # If we delay by 1 picosecond, then it's as if each level is
    # moved one to the right. so add the delay to the level
    # for collision calculation
    total_severity = sum(
        1
        for level_n, level_range in levels.items()
        if (level_n+delay) % ((2*(level_range-2))+2) == 0
    )

    return total_severity


for delay in count():
    if get_severity(delay) == 0:
        break
print delay