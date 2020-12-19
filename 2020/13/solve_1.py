fname = "input.txt"
# fname = "test_input1.txt"

with open(fname) as fandle:
    me_arrive = int(fandle.readline())
    bus_ids = [
        int(i)
        for i in fandle.readline().split(',')
        if i != 'x'
    ]

wait_times_and_ids = sorted(
        (bus_id - (me_arrive % bus_id), bus_id)
        for bus_id in bus_ids
)

soonest = wait_times_and_ids[0]
print(soonest[0] * soonest[1])
