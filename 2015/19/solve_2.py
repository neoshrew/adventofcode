from collections import defaultdict


transitions = defaultdict(list)


fname = 'input.txt'
#fname = 'input_test.txt'
#fname = 'input_test_2.txt'
with open(fname) as fandle:
    for line in fandle:
        line = line.strip()
        if not line:
            continue
        parts = line.split()

        if len(parts) == 3:
            transitions[parts[0]].append(parts[2])

        if len(parts) == 1:
            end_molecule = line

start_mol = 'e'

# And let's reduce from end to start.
end_molecule, start_mol = start_mol, end_molecule
_transitions = defaultdict(list)
for k, v in transitions.items():
    for _v in v:
        _transitions[_v].append(k)
transitions = _transitions
del _transitions
#for k, v in transitions.items():
#    print k, '=>', v

def get_mol_positions(mol_pattern, all_mols):
    index = None
    while True:
        index = all_mols.find(mol_pattern, index)
        if index == -1:
            break
        yield index
        index += 1

# So I've tried to BFS this, however the number of
# possibilites makes it ridiculously long to compute.
# However, as the thread in the subreddit pointed out
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
# The problem has an interesting property which I admit I don't fully
# understand. The short of it is that People have discovered that
# doing a greed DFS search seems to get them the correct answer.
# So the CS nerd in me is irritated because I cannot prove that this
# is correct, because I am too dumb to understand this property.

transitions = sorted(transitions.items(), key=lambda x: -len(x[0]))

depth = 0
_mol = start_mol
while True:
    for trans_start, trans_end in transitions:
        index = _mol.find(trans_start)
        if index == -1:
            continue
        end = trans_end[0]
        _mol = _mol[:index] + end + _mol[index+len(trans_start):]
        depth += 1
        break

    else:
        # didn't find another transition
        break

if _mol == end_molecule:
    print depth
else:
    print "failed"


# Yep. That worked. I guess the transitons are modelled such that
# if you were to generate a pattern starting at e using the forward
# transitions, your options are more tree-like, so doing the reverse
# becomes more like searching back up the tree rather than a full
# graph search.
# I presume there's a proof for this.