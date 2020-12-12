with open("input.txt") as fandle:
    numbers = [int(i) for i in fandle if i]

def thing(target):
    # There's probably a clever way to do this, but I'm lazy
    for ia, a in enumerate(numbers):
        for ib, b in enumerate(numbers[ia:], ia):
            for c in numbers[ib:]:
                if a + b + c == target:
                    return a*b*c

print(thing(2020))
