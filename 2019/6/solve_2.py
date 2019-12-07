with open("input.txt") as fandle:
    orbits = {
        k: v for v, k in (line.strip().split(")") for line in fandle if line)
    }

# s="""COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""
# orbits = {
#     k: v for v, k in (line.strip().split(")") for line in s.split('\n') if line)
# }



BASE = 'COM'

def get_to_node(node):
    path = []
    while node != BASE:
        node = orbits[node]
        path.append(node)
    return path[::-1]

santa_path = get_to_node('SAN')
you_path = get_to_node('YOU')

shared_base = sum(
    1 if san == you else 0
    for san, you in zip(santa_path, you_path)
)

print(len(santa_path) + len(you_path) - 2*shared_base)
