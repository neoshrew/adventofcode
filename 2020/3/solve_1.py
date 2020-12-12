fname = "input.txt"
# fname = "test_input1.txt"

tree = '#'
rightstep = 3
total = 0
curr_x = 0
with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        if line[curr_x] == tree:
            total += 1
        curr_x = (curr_x + rightstep) % len(line)

print(total)
