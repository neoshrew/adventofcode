import sys

with open('input.txt') as fandle:
    data = fandle.read()


def get_garbage_chars(data):
    in_garbage = False
    garbage_chars = 0
    index = 0

    while index < len(data):
        char = data[index]
        if char == '!':
            # ignore the next character
            index += 2
            continue

        if in_garbage:
            if char == '>':
                in_garbage = False
            else:
                garbage_chars += 1

        elif char == '<':
            in_garbage = True

        index += 1

    return garbage_chars


if False:
    for i in [
        '<>',
        '<random characters>',
        '<<<<>',
        '<{!>}>',
        '<!!>',
        '<!!!>>',
        '<{o"i!a,<{i<a>',
    ]:
        print i, get_garbage_chars(i)

print get_garbage_chars(data)
