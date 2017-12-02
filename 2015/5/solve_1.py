fname = 'test_input_1.txt'
fname = 'input.txt'
with open(fname) as fandle:
    names = [i.strip() for i in fandle if i.strip()]


vowels = 'aeiou'
bad_strings = {'ab', 'cd', 'pq', 'xy'}

total = 0
for name in names:
    # has to contain at least three vowels
    if sum(1 if i in vowels else 0 for i in name) < 3:
        continue

    char_pairs = set(''.join(i) for i in zip(name, name[1:]))

    # has to contain at least one pair
    for pair in char_pairs:
        if pair[0] == pair[1]:
            break

    else:
        continue

    if bad_strings & char_pairs:
        continue

    total += 1

print total