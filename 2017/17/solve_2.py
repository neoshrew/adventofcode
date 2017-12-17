with open('input.txt') as fandle:
    jump_size = int(fandle.read())

steps = 50000000


val = None
pos = 0
# Don't remember the whole buffer, just remember what we put after 0.
# 0 is always going to remain in index 0, so if pos == 0, we're going
# to insert something after 0, so remember that value.
for i in xrange(1, steps+1):
    pos += jump_size
    pos %= i

    if pos == 0:
        val = i

    pos += 1


print val
