import re, math
from collections import defaultdict

fname = "input.txt"
# fname = "test_2.txt"

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

total_ore = 0
excess_amounts = defaultdict(int)
queue = [(1, "FUEL")]
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

print(total_ore)
