with open('input.txt') as fandle:
    jump_size = int(fandle.read())

steps = 2017


buffer = [0]
pos = 0

for i in xrange(1, steps+1):
    pos += jump_size
    pos %= i
    buffer.insert(pos+1, i)
    pos += 1

print buffer[pos+1]