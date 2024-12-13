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

    checked_id = max([block[0] for block in blocks if block[0] is not None])+1
    block_pos = len(blocks) -1
    for block_pos in range(len(blocks)-1, -1, -1):
        this_block = blocks[block_pos]
        if this_block[0] is None or this_block[0] >= checked_id:
            block_pos -= 1
            continue

        for i in range(block_pos):
            if blocks[i][0] is None and blocks[i][1] >= this_block[1]:
                # i is where we need to put our current block. But first
                # let's cut out the curent block_pos
                blocks.pop(block_pos)
                if blocks[block_pos-1][0] is None:
                    # previous block is empty, so extend that
                    blocks[block_pos-1][1] += this_block[1]
                    # was the next block empty? in which case fold that in
                    if len(blocks) > block_pos and blocks[block_pos][0] is None:
                        blocks[block_pos-1][1] += blocks.pop(block_pos)[1]
                elif len(blocks) > block_pos and blocks[block_pos][0] is None:
                    # fold the new empty space into the next empty block
                    blocks[block_pos][1] += this_block[1]
                elif len(blocks) > block_pos:
                    # We've got no empty space either side, so insert some
                    blocks.insert(block_pos, [None, this_block[1]])
                # else: len(blocks) <= i - we're at the end so doesn't matter

                blocks[i][1] -= this_block[1]
                if blocks[i][1] == 0:
                    blocks.pop(i)

                blocks.insert(i, this_block)
                break

        checked_id -= 1


    # print(''.join(
    #     (str(block[0]) if block[0] is not None else '.')*block[1]
    #     for block in blocks
    # ))
    checksum = 0
    pos = 0
    for block in blocks:
        if block[0] is not None:
            checksum += sum(
                block[0]*pos_
                for pos_ in range(pos, pos+block[1])
            )
        pos += block[1]
    print(checksum)

if __name__ == "__main__":
    main()