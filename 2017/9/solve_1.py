import sys

with open('input.txt') as fandle:
    data = fandle.read()


def get_score(data):
    in_garbage = False
    total_score = 0
    current_score = 0
    index = 0

    while index < len(data):
        char = data[index]
        if char == '!':
            # ignore the next character
            index += 1
        elif in_garbage:
            if char == '>':
                in_garbage = False
        elif char == '<':
            in_garbage = True
        elif char == '{':
            current_score += 1
        elif char == '}' and current_score > 0:
            total_score += current_score
            current_score -= 1

        index += 1

    return total_score

if False:
    for i in [
        '{}',
        '{{{}}}',
        '{{},{}}',
        '{{{},{},{{}}}}',
        '{<{},{},{{}}>}',
        '{<a>,<a>,<a>,<a>}',
        '{{<a>},{<a>},{<a>},{<a>}}',
        '{{<!>},{<!>},{<!>},{<a>}}',
        '{}',
        '{{{}}}',
        '{{},{}}',
        '{{{},{},{{}}}}',
        '{<a>,<a>,<a>,<a>}',
        '{{<ab>},{<ab>},{<ab>},{<ab>}}',
        '{{<!!>},{<!!>},{<!!>},{<!!>}}',
        '{{<a!>},{<a!>},{<a!>},{<ab>}}',
    ]:
        print i, get_score(i)

print get_score(data)
