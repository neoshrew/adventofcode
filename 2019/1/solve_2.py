# take its mass, divide by three, round down, and subtract 2.

def fuel_for_module(mod_mass):
    total = 0
    to_add = mod_mass//3 - 2
    while to_add > 0:
        total += to_add
        x = to_add
        to_add = to_add//3 - 2

    return total


with open('input.txt') as fandle:
    total = sum(
        fuel_for_module(int(line))
        for line in fandle
        if line.strip()
    )

print(total)
