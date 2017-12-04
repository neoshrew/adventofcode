from operator import lt, gt
from functools import partial

lt = partial(partial, lt)
gt = partial(partial, gt)


the_aunt = {
    'children': 3,
    'cats': lt(7),
    'samoyeds': 2,
    'pomeranians': gt(3),
    'akitas': 0,
    'vizslas': 0,
    'goldfish': gt(5),
    'trees': lt(3),
    'cars': 2,
    'perfumes': 1,
}
keys = set(the_aunt)

def sub_dict_cmp(aunt_data):
    for key in keys & set(aunt_data):
        to_cmp = the_aunt[key]
        if isinstance(to_cmp, int):
            if aunt_data[key] != to_cmp:
                return False
        else:
            if not to_cmp(aunt_data[key]):
                return False

    return True

with open('input.txt') as fandle:
    for line in fandle:
        if sub_dict_cmp(dict(
            (data[0], int(data[1]))
            for data in (
                part.split(': ')
                for part in line.strip().split(': ', 1)[1].split(', ')
            )
        )):
            print line.split(':', 1)[0].split()[1]