import re

fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input2.txt"

MY_BAG = "shiny gold"

# wavy fuchsia bags contain 1 bright cyan bag, 5 pale violet bags, 5 muted maroon bags.
RE = re.compile("(\d+) ([a-z ]+?) bags?[,.]")

def parse_line(line):
    bag_desc, all_content = line.split(" bags contain ")
    contents = {
        inner_bag_desc: int(amount)
        for amount, inner_bag_desc in RE.findall(all_content)
    }
    return bag_desc, contents

with open(fname) as fandle:
    graph = {
        bag_desc: contents
        for bag_desc, contents in (
            parse_line(line.rstrip())
            for line in fandle
        )
    }

cache = {}
def get_bag_content_count(bag_desc):
    # returns a count of number of bags a bag must contain,
    if bag_desc in cache:
        return cache[bag_desc]

    total = 0
    for inner_bag_desc, amount in graph[bag_desc].items():
        total += amount
        total += get_bag_content_count(inner_bag_desc) * amount

    return total

print(get_bag_content_count(MY_BAG))
