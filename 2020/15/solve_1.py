NTH_NUMBER=2020

TESTS = [
    ("0,3,6", 436),
    ("1,3,2", 1),
    ("2,1,3", 10),
    ("1,2,3", 27),
    ("2,3,1", 78),
    ("3,2,1", 438),
    ("3,1,2", 1836),
]

INPUT = "13,0,10,12,1,5,8"

def get_nth_number(starting_numbers, nth_number):
    numbers = {}

    for curr_pos, number in enumerate(starting_numbers, 1):
        numbers[number] = (None, curr_pos)

    # All given examples don't have repeats in the starting numbers.
    # Simple check for that here.
    assert len(numbers) == len(starting_numbers)

    last_number = starting_numbers[-1]

    for curr_pos in range(curr_pos+1, nth_number+1):
        curr_n_second_to_last, curr_n_last = numbers[last_number]
        if curr_n_second_to_last is None:
            new_n = 0
        else:
            new_n = curr_n_last - curr_n_second_to_last

        if new_n in numbers:
            numbers[new_n] = numbers[new_n][1], curr_pos
        else:
            numbers[new_n] = (None, curr_pos)

        last_number = new_n

    return last_number


def parse_raw_numbers(raw_numbers):
    return [int(i) for i in raw_numbers.split(',')]

def get_nth_number_raw(raw_numbers, nth_number):
    return get_nth_number(parse_raw_numbers(raw_numbers), nth_number)

# for raw_numbers, expected in TESTS:
#     result = get_nth_number_raw(raw_numbers, NTH_NUMBER)
#     print(expected == result, expected, result, raw_numbers)

print(get_nth_number_raw(INPUT, NTH_NUMBER))
