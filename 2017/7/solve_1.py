#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
things = dict()
weights = dict()
with open('input.txt') as fandle:
    for line in fandle:
        parts = line.split()
        name = parts[0]
        weights[name] = int(parts[1][1:-1])
        things[name] = [i.replace(',', '') for i in parts[3:]]

# the bottom program is simply the only one without a references to it.
all_prog_names = set(things)
referenced_names = set(
    ref
    for item_refs in things.values()
    for ref in item_refs
)

print list(all_prog_names - referenced_names)[0]