from itertools import groupby

with open("input.txt") as fandle:
    pin_min, pin_max = map(int, fandle.readline().split('-'))

def is_valid(number):
    l = '0'
    found_pair = False
    for n, c in groupby(str(number)):
        if n < l:
            return False
        l = n

        if len(list(c)) == 2:
            found_pair = True

    return found_pair

total = sum(is_valid(i) for i in range(pin_min, pin_max+1))

print(total)
