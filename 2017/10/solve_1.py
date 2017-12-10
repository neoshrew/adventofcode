with open('input.txt') as fandle:
    lengths = [int(i) for i in fandle.read().split(',')]

def hash(lengths, lsize=256):
    vals = list(range(lsize))

    skip = 0
    index = 0
    for length in lengths:
        i, j = index, index+length

        if j >= lsize:
            _vals = (vals[i:] + vals[:j%lsize])[::-1]
            vals[i:] = _vals[:lsize-i]
            vals[:j%lsize] = _vals[lsize-i:]
        else:
            vals[i:j] = vals[i:j][::-1]

        index += length + skip
        skip += 1
        if index >= lsize:
            index = index % lsize

    return vals


hash_vals = hash(lengths)
print hash_vals[0] * hash_vals[1]