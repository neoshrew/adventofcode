fname = "input.txt"
# fname = "test_input1.txt"

slopes = {
    gradient: [0, 0] # total, curr_x
    for gradient in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
}
tree = '#'

with open(fname) as fandle:
    for depth, line in enumerate(fandle):
        line = line.rstrip()

        for (grad_x, grad_y), vals in slopes.items():
            if depth % grad_y != 0:
                continue
            if line[vals[1]] == tree:
                vals[0] += 1
            vals[1] = (vals[1] + grad_x) % len(line)

total = 1
for slope_total, _ in slopes.values():
    total *= slope_total

print(total)
