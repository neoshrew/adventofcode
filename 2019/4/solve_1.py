with open("input.txt") as fandle:
    pin_min, pin_max = map(int, fandle.readline().split('-'))

def is_valid(number):
    as_str = str(number)
    found_pair = False
    for i, c in enumerate(as_str[1:]):
        # The character points are ordered the same as the numers
        lc = as_str[i]
        if lc > c:
            return False

        if lc == c:
            found_pair = True

    return found_pair

total = sum(is_valid(i) for i in range(pin_min, pin_max+1))

print(total)
