FNAME = "input.txt"
# FNAME = "test1.txt"

def get_blocks():
    blocks = []
    id_, isfile = 0, True
    with open(FNAME) as fandle:
        for c in fandle.read():
            if not c.isdigit():
                continue
            c = int(c)

            if isfile:
                blocks.append([id_, c])
                id_ += 1
                isfile = False
            else:
                blocks.append([None, c])
                isfile = True

    return blocks

def main():
    blocks = get_blocks()

    checksum = 0
    pos = 0
    while True:
        # If we ever end up with 0-sized blocks on either end, drop them
        while blocks and blocks[0][1] == 0:
            blocks.pop(0)
        # as well as dropping empty blocks at the end
        while blocks and (blocks[-1][1] == 0 or blocks[-1][0] is None):
            blocks.pop(-1)

        if not blocks:
            break

        if blocks[0][0] is None: # current block is empty space
            # free space, so take a block from the last file
            checksum += blocks[-1][0] * pos
            blocks[-1][1] -= 1

        else: # current block already has data
            checksum += blocks[0][0] * pos

        # mark the space in the current block as processed
        blocks[0][1] -= 1
        # increase our curent position pointer
        pos += 1

    print(checksum)

if __name__ == "__main__":
    main()