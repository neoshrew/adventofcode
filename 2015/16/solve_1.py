the_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}
keys = set(the_aunt)

def sub_dict_cmp(aunt_data):
    for key in keys & set(aunt_data):
        if aunt_data[key] != the_aunt[key]:
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