from collections import defaultdict

transitions = defaultdict(list)


fname = 'input.txt'
#fname = 'input_test.txt'
with open(fname) as fandle:
    for line in fandle:
        line = line.strip()
        if not line:
            continue
        parts = line.split()

        if len(parts) == 3:
            transitions[parts[0]].append(parts[2])

        if len(parts) == 1:
            start_molecule = line

# split the starting molecule up into its molecules for ease.
# e.g. HHOTi is 4 molecules H H O and Ti
_start_molecules = []
for i in start_molecule:
    if i.upper() == i:
        _start_molecules.append(i)
    else:
        _start_molecules[-1] = _start_molecules[-1] + i

start_molecules = tuple(_start_molecules)
del _start_molecules


def get_molecule_positions(molecule):
    for index, mol in enumerate(start_molecules):
        if mol == molecule:
            yield index


seen = set()

for this_mol, end_mols in transitions.items():
    for pos in get_molecule_positions(this_mol):
        for mol in end_mols:
            seen.add(''.join(start_molecules[:pos] + (mol,) + start_molecules[pos+1:]))

print len(seen)
