import re

with open("input.txt") as fandle:
    line = fandle.readline()

match = re.search("row ([0-9]+), column ([0-9]+)\.", line)

row = int(match.groups()[0])
column = int(match.groups()[1])

def get_seq_n(row, col):
    n = row + col - 1
    base = (n*(n-1))//2
    return base + col


def get_seq_n_val(n):
    # This is a terrible brute force...
    s = 20151125
    for _ in range(n-1):
        s *= 252533
        s %= 33554393
    return s

# for i in range(1, 7):
#     for j in range(1, 7):
#         print("{:12d}".format(get_seq_n_val(get_seq_n(i, j))), end="")
#     print()

print(get_seq_n_val(get_seq_n(row, column)))
