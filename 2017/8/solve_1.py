import operator
from collections import defaultdict

registers = defaultdict(int)


opmap = {
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}

def eval_clause(clause):
    in1, op, in2 = clause

    try:
        in1 = int(in1)
    except ValueError:
        in1 = registers[in1]
    try:
        in2 = int(in2)
    except ValueError:
        in2 = registers[in2]

    return opmap[op](in1, in2)


with open('input.txt') as fandle:
    for line in fandle:
        parts = line.split()
        if eval_clause(parts[4:]):
            value = int(parts[2])
            if parts[1] == 'dec':
                registers[parts[0]] -= value
            else:
                registers[parts[0]] += value

print max(registers.values())
