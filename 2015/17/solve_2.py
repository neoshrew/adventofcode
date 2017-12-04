from collections import defaultdict

amount = 150
with open('input.txt') as fandle:
    containers = [int(i) for i in fandle]

total = 0
ways = defaultdict(int)
fmt = "{{:0{:d}b}}".format(len(containers))
for i in range(2**len(containers)):
    wanted_containers = [
        container
        for bin_val, container in zip(fmt.format(i), containers)
        if bin_val == '1'
    ]

    if sum(wanted_containers) == amount:
        total += 1
        ways[len(wanted_containers)] += 1

print sorted(ways.items())[0][1]