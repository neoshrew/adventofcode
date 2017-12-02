
def next_look_and_say(val):
    new_chars = []

    char = val[0]
    count = 0
    for i in val:
        if i != char:
            new_chars.append(str(count))
            new_chars.append(char)
            count = 0
            char = i

        count += 1

    new_chars.append(str(count))
    new_chars.append(char)
    return ''.join(new_chars)


with open('input.txt') as fandle:
    val = fandle.read().strip()


for i in range(50):
    val = next_look_and_say(val)
print len(val)