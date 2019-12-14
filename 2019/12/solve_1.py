from copy import deepcopy
import re

fname, TARGET_STEPS = "input.txt", 1000
# fname, TARGET_STEPS = "test_1.txt", 10
with open(fname) as fandle:
    MOONS = [
        [tuple(int(i) for i in match), (0,)*3]
        for match in (
            re.findall("-?[0-9]+", line)
            for line in fandle
        )
        if match
    ]


def addtriple(trip1, trip2):
    return tuple(i+j for i, j in zip(trip1, trip2))

def velocity_effects(pos1, pos2):
    effect_1 = tuple(
        0 if a == b else 1 if a < b else -1
        for a, b in zip(pos1, pos2)
    )
    effect_2 = tuple(-i for i in effect_1)
    return effect_1, effect_2


def step(moons):
    new_moons = deepcopy(moons[::])
    for a, (moon_a, _) in enumerate(moons):
        for b, (moon_b, _) in enumerate(moons[a+1:], a+1):
            eff_a, eff_b = velocity_effects(moon_a, moon_b)
            new_moons[a][1] = addtriple(new_moons[a][1], eff_a)
            new_moons[b][1] = addtriple(new_moons[b][1], eff_b)

    for i, (pos, vel) in enumerate(new_moons):
        new_moons[i][0] = addtriple(pos, vel)

    return new_moons

for _ in range(TARGET_STEPS):
    MOONS = step(MOONS)

energy = sum(
    sum(abs(j) for j in pos) * sum(abs(j) for j in vel)
    for pos, vel in MOONS
)

print(energy)
