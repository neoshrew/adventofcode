from itertools import count

with open('input.txt') as fandle:
    instructions = [int(i) for i in fandle]

index = 0
try:
    # count starts at 0, when we loop again we count the last instuction.
    # the IndexError will be raised when trying to execude the first
    # instruction outside of the list.
    for steps in count():
        jump = instructions[index]
        instructions[index] += 1
        index += jump

except IndexError:
    pass

print steps
