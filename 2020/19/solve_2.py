import re

fname = "input.txt"
# fname = "test_input2.txt"


RAW_RULES = {}
RE_RULES = {}
final_re = re.compile('"([ab])"')

def parse_targets(targets):
    return tuple(
        tuple(chunk.split())
        for chunk in targets.split(" | ")
    )

with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        if not line:
            break

        source, targets = line.split(': ')

        if (match := final_re.match(targets)) is not None:
            RE_RULES[source] = match.groups()[0]

        else:
            RAW_RULES[source] = parse_targets(targets)

    POTENTIALS = [line.rstrip() for line in fandle]

def generate_re(from_):
    if from_ in RE_RULES:
        return RE_RULES[from_]

    # Stop infinite recurstion
    RE_RULES[from_] = None

    chunks = [
        [generate_re(i) for i in chunk]
        for chunk in RAW_RULES[from_]
    ]
    for chunk in chunks:
        for i in chunk:
            if i is None:
                # Can't generate a regex
                return None

    re_str = "({})".format("|".join(
        "".join(i for i in chunk)
        for chunk in chunks
    ))

    RE_RULES[from_] = re_str
    return re_str

# I'm lazy, and even the question says
#   (Remember, you only need to handle the rules you have; building a solution
#   that could handle any hypothetical combination of rules would be
#   significantly more difficult.)
# from my input(s) I can see that 8 and 11 are only used in 1.
# Lets do something dumb

# 8: 42 | 42 8
RAW_RULES["8"] = parse_targets("42 | 42 8")
# 11: 42 31 | 42 11 31
RAW_RULES["11"] = parse_targets("42 31 | 42 11 31")


# 8 is basically 42+ - i.e. one or more instances of 42
RE_RULES["8"] = "({}+)".format(generate_re("42"))

# ...I'm really sorry, please don't judge me.
_cache = {}
def _gen_re(level):
    # level starts from 0, and denotes the level of recursion we're
    # checking for 11. This is terrible.
    if level in _cache:
        return _cache[level]

    # 11: 42 31 | 42 11 31
    component_11 = (generate_re("42")*(level+1)) + (generate_re("31")*(level+1))
    # 0: 8 11
    component_0 = "^{}{}$".format(RE_RULES["8"], component_11)

    _cache[level] = re.compile(component_0)
    return _cache[level]

total = 0
for j, potential in enumerate(POTENTIALS):
    # len(potential/2) as an upper limit... what have I become?
    for i in range(len(potential)//2):
        if _gen_re(i).match(potential):
            total += 1
            break

print(total)

# This took 7.5 seconds to run. I'm a terrible engineer.
