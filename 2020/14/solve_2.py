fname = "input.txt"
# fname = "test_input2.txt"


word_size = 36
word_format_str = "{{:0{:d}b}}".format(word_size)
# We need two bitwise masks.
# - to set to 1 we need to OR with the 1s
# - to set to 0 we need to AND with the Xs replaced with 1s
maskOR = 2**36-1
maskAND = 2**36-1
mem = {}


program = []
with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        cmd, operand = line.split(" = ")

        if cmd == "mask":
            program.append((cmd, operand))

        else: # cmd.startswith("mem[")
            mem_loc = int(cmd[4:-1])
            operand = int(operand)
            program.append(("mem", mem_loc, operand))

def generate_mem_locations(mask, loc):
    new_mask = [
        'X' if mask_char == 'X' else '1' if mask_char == '1' else loc_char
        for mask_char, loc_char in zip(mask, word_format_str.format(loc))
    ]
    variable_locs = [i for i, c in enumerate(new_mask) if c == 'X']

    for i in range(2**len(variable_locs)):
        istr = "{{:0{:d}b}}".format(len(variable_locs)).format(i)
        for loc, new_chr in zip(variable_locs, istr):
            new_mask[loc] = new_chr
        yield int("".join(new_mask), 2)

current_mask = None
for cmd, *operands in program:
    if cmd == "mask":
        current_mask = operands[0]

    else: # cmd == "mem"
        loc, value = operands
        for loc in generate_mem_locations(current_mask, loc):
            mem[loc] = value

print(sum(mem.values()))
