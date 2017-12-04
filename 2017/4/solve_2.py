total = 0
with open('input.txt') as fandle:
    for line in fandle:
        parts = [''.join(sorted(word)) for word in line.split()]
        if len(parts) == len(set(parts)):
            total += 1

print total