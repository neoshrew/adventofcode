#!/usr/bin/env python

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test1.txt"

def read_input():
    all_elfs = []
    curr_elf = []
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if not line and curr_elf:
                all_elfs.append(curr_elf)
                curr_elf = []
            else:
                curr_elf.append(int(line))
    if curr_elf:
        all_elfs.append(curr_elf)
    return all_elfs

def main():
    totals = [sum(i) for i in read_input()]
    top_3 = sorted(totals)[-3:]
    print(sum(top_3))

if __name__ == "__main__":
    main()
