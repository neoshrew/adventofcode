fname = "input.txt"
# fname = "test_input1.txt"


word_size = 36
# We need two bitwise masks.
# - to set to 1 we need to OR with the 1s
# - to set to 0 we need to AND with the Xs replaced with 1s
maskOR = 2**36-1
maskAND = 2**36-1
mem = {}



with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        cmd, operand = line.split(" = ")

        if cmd == "mask":
            maskOR = int(operand.replace('X', '0'), 2)
            maskAND = int(operand.replace('X', '1'), 2)

        else: # cmd.startswith("mem[")
            mem_loc = int(cmd[4:-1])
            operand = int(operand)
            mem[mem_loc] = (operand | maskOR) & maskAND

print(sum(mem.values()))
