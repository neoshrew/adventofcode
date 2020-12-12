with open("input.txt") as fandle:
    numbers = set(int(i) for i in fandle if i)

target = 2020

for number in numbers:
    other = target - number
    if other in numbers:
        print(number*other)
        break
