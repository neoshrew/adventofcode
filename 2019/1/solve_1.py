# take its mass, divide by three, round down, and subtract 2.

with open('input.txt') as fandle:
    print(sum(
        int(line)//3 - 2
        for line in fandle
        if line.strip()
    ))
