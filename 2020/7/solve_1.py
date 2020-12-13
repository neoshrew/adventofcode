from collections import defaultdict
import re

fname = "input.txt"
# fname = "test_input1.txt"

MY_BAG = "shiny gold"

# wavy fuchsia bags contain 1 bright cyan bag, 5 pale violet bags, 5 muted maroon bags.
RE = re.compile("(\d+) ([a-z ]+?) bags?[,.]")

def parse_line(line):
    bag_desc, all_content = line.split(" bags contain ")
    contents = tuple(
        (int(amount), inner_bag_desc)
        for amount, inner_bag_desc in RE.findall(all_content)
    )
    return bag_desc, contents

with open(fname) as fandle:
    # Let's build the inverse graph unweighted
    graph = defaultdict(set)
    for line in fandle:
        bag_desc, contents = parse_line(line.rstrip())
        for _, content_bag_desc in contents:
            graph[content_bag_desc].add(bag_desc)

q = [MY_BAG]
seen = set()
can_contain = set()

while q:
    curr = q.pop(0)
    if curr in seen:
        continue
    can_contain.update(graph[curr])
    q.extend(graph[curr])
    seen.add(curr)

print(len(can_contain))
