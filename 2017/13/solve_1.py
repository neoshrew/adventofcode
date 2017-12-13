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

# each later has a cycle of 2*(range-2) + 2
# if that cycle is a factor of its level, then it will collide.
total_severity = sum(
    level_n * level_range
    for level_n, level_range in levels.items()
    if level_n % ((2*(level_range-2))+2) == 0
)
print total_severity
