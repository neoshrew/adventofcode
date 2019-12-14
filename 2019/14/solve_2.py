import re, math
from collections import defaultdict

fname = "input.txt"
# fname = "test_2.txt"
# fname = "test_3.txt" #13312

RE = re.compile("([0-9]+) ([A-Z]+)")
def parse_line(line):
    match = RE.findall(line)
    items = [
        (int(i[0]), i[1])
        for i in match
    ]
    result_amount, result_name = items.pop()

    return result_name, (result_amount, items)

with open(fname) as fandle:
    reactions = {
        k: v
        for k, v in (
            parse_line(line)
            for line in fandle
            if line.strip()
        )
    }


def amt_for_fuel(fuel_amt):
    total_ore = 0
    excess_amounts = defaultdict(int)
    queue = [(fuel_amt, "FUEL")]
    while queue:
        curr_needed, curr_item = queue.pop(0)

        if excess_amounts[curr_item] >= curr_needed:
            excess_amounts[curr_item] -= curr_needed
            continue

        curr_needed -= excess_amounts[curr_item]
        excess_amounts[curr_item] = 0

        reaction_amount, reagents = reactions[curr_item]
        needed_reactions = math.ceil(curr_needed/reaction_amount)
        excess_amounts[curr_item] += (needed_reactions*reaction_amount) - curr_needed
        for reagent_amount, reagent_name in reagents:
            if reagent_name == 'ORE':
                total_ore += needed_reactions * reagent_amount
            else:
                queue.append((reagent_amount*needed_reactions, reagent_name))

    return(total_ore)

target_ore = 1000000000000
pow = 3
while True:
    if amt_for_fuel(10**pow) > target_ore:
        break
    pow += 1

lower = 10**(pow-1)
upper = 10**(pow)
while True:
    mid = (lower+upper)//2
    if mid == lower:
        break
    amt = amt_for_fuel(mid)
    if amt < target_ore:
        lower = mid
    else:
        upper = mid

print(mid)
