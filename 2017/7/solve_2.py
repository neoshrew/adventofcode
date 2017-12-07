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

all_prog_names = set(things)
referenced_names = set(
    ref
    for item_refs in things.values()
    for ref in item_refs
)

base = list(all_prog_names - referenced_names)[0]

sum_of_weights = dict()
all_unbalanced = list()
def pop_sum_of_weights(prog, level=0):
    if prog not in sum_of_weights:
        child_weights = [pop_sum_of_weights(i, level+1) for i in things[prog]]
        sum_of_weights[prog] = sum(child_weights) + weights[prog]

        if child_weights and len(set(child_weights)) != 1:
            all_unbalanced.append((level, prog))

    return sum_of_weights[prog]

pop_sum_of_weights(base)

unbalanced = sorted(all_unbalanced)[-1][1]

unbalanced_children = things[unbalanced]
unbal_child_weights = [sum_of_weights[k] for k in unbalanced_children]
for child in unbalanced_children:
    if unbal_child_weights.count(sum_of_weights[child]) == 1:
        curr_weight = sum_of_weights[child]
        unbal_child_weights.remove(curr_weight)
        required_weight = unbal_child_weights[0]

        break

change_required = required_weight - curr_weight
print weights[child] + change_required