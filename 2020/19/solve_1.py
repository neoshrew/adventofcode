import re

fname = "input.txt"
# fname = "test_input1.txt"


RAW_RULES = {}
RE_RULES = {}
final_re = re.compile('"([ab])"')
with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        if not line:
            break

        source, targets = line.split(': ')

        if (match := final_re.match(targets)) is not None:
            RE_RULES[source] = match.groups()[0]

        else:
            # "1: 2 3 | 3 2"
            # -> "1": (("1","2"), ("3", "2"))

            RAW_RULES[source] = tuple(
                tuple(chunk.split())
                for chunk in targets.split(" | ")
            )

    POTENTIALS = [line.rstrip() for line in fandle]

def generate_re(from_):
    if from_ in RE_RULES:
        return RE_RULES[from_]

    re_str = "({})".format("|".join(
        "".join(generate_re(i) for i in chunk)
        for chunk in RAW_RULES[from_]
    ))


    RE_RULES[from_] = re_str
    return re_str

THE_RE = re.compile("^{}$".format(generate_re("0")))

total = 0
for potential in POTENTIALS:
    if THE_RE.match(potential):
        total += 1

print(total)
