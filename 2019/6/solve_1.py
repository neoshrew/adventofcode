with open("input.txt") as fandle:
    orbits = {
        k: v for v, k in (line.strip().split(")") for line in fandle if line)
    }

tree = {}
for child, parent in orbits.items():
    if parent not in tree:
        tree[parent] = set()
    tree[parent].add(child)

# Centre Of Mass is the marent
curr_gen = ["COM"]
curr_gen_n = 0
orbits = 0
while curr_gen:
    orbits += curr_gen_n * len(curr_gen)
    curr_gen_n += 1
    curr_gen = [
        next_gen_node
        for node in curr_gen
        if node in tree
        for next_gen_node in tree[node]
    ]

print(orbits)
