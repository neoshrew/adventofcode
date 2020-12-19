fname = "input.txt"
# fname = "test_input1.txt"

tests = [
    ("7,13,x,x,59,x,31,19", 1068781),
    ("17,x,13,19", 3417),
    ("67,7,59,61", 754018),
    ("67,x,7,59,61", 779210),
    ("67,7,x,59,61", 1261476),
    ("1789,37,47,1889", 1202161486),
]

with open(fname) as fandle:
    fandle.readline()
    input_raw = fandle.readline()

def parse_raw_input(input_raw):
    return [
        (int(bus_id_raw), lag_time)
        for lag_time, bus_id_raw in enumerate(input_raw.split(','))
        if bus_id_raw != 'x'
    ]

def parse_congruencies(input_data):
    # i.e T ≡ time_since_last_arrival (mod bus_id)
    # time_since_last_arrival is bus_id - lag_time
    # but special case the first one as that would always be 0

    # "This method is faster if the moduli have been ordered by decreasing value"
    return sorted([(0, input_data[0][0])] + [
        (bus_id - (lag_time%bus_id), bus_id)
        for bus_id, lag_time in input_data[1:]
    ], reverse=True)

# I cheated for this and looked at Reddit becuase I had no ideas.
# Reddit pointed me to the wikipedia page on the Chinese remainder theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
# I didn't really grok using the existence construction, so trying the
# sieve first.

def mycounter(start, step):
    while True:
        yield start
        start += step

def solve_congruencies(congruencies):
    print(congruencies)
    x, n = congruencies[0]
    for cg in congruencies[1:]:
        print(congruencies.index(cg), "/", len(congruencies))
        for nx in mycounter(x, n):
            if nx % cg[1] == cg[0]:
                break
        x = nx
        n *= cg[1]

    return x

def solve_raw_data(input_raw):
    data = parse_raw_input(input_raw)
    congruencies = parse_congruencies(data)
    return solve_congruencies(congruencies)

if False:
    for test_data_raw, expected_result in tests:
        actual_result = solve_raw_data(test_data_raw)
        print(actual_result==expected_result, actual_result,
            expected_result, test_data_raw)

print(solve_raw_data(input_raw))
