from itertools import tee, izip

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


# lower case letters except for i, o, and l
CHARS = 'abcdefghjkmnpqrstuvwxyz'
CHARS_SET = set(CHARS)
def incr(password):
    if not password:
        return 'a'

    next = CHARS.index(password[-1]) + 1
    if next >= len(CHARS):
        return incr(password[:-1]) + CHARS[0]
    return password[:-1] + CHARS[next]


def password_iter(start=''):
    while True:
        start = incr(start)
        yield start


with open('input.txt') as fandle:
    START_PASSWORD = fandle.read().strip()

def check_potential(potential):
    if set(potential) - CHARS_SET:
        return False

    count = 1
    last_chr = potential[0]
    for chr in potential[1:]:
        if ord(last_chr) +1 == ord(chr):
            count += 1
        else:
            count = 1
        last_chr = chr
        if count == 3:
            break

    if count < 3:
        return False

    for i, first_pair in enumerate(pairwise(potential), 2):
        if first_pair[0] != first_pair[1]:
            continue

        for second_pair in pairwise(potential[i:]):
            if second_pair[0] != second_pair[1]:
                continue

            if first_pair != second_pair:
                return True

    return False

for potential in password_iter(START_PASSWORD):
    if check_potential(potential):
        print potential
        break