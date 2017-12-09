from itertools import count
from math import floor


# I don't know why I do this for every one...
with open('input.txt') as fandle:
    total_presents = int(fandle.read())

# Let's divide by 10, because that makes it easier.
total_presents /= 10

# So we want to find the first number, whereby the
# sum of its unique factors is equal to our input
# number (because we divided by 10.)
# Beacuse each house is visited by elves assigned a number
# which is a factor of the house.
def factor_a_number(a_number):
    factors = [1, a_number]

    # x**.5 is x^.5 which is sqrt(x).
    # according to my test, **.5 is 3x faster
    # than math.sqrt()
    bound = int(floor((a_number**.5)+1))
    for i in range(2, bound):
        if a_number % i == 0:
            factors.append(i)
            factors.append(a_number//i)

    return set(factors)

# This works, but took about 22 seconds on my 4th gen i7
for i in count(1):
    factors = factor_a_number(i)
    sum_ = sum(factors)
    if sum_ >= total_presents:
        break
print i