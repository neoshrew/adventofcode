from operator import xor


with open('input.txt') as fandle:
    hash_key = fandle.read().strip()


_lengths = [17, 31, 73, 47, 23]
def hash(string, lsize=256, _nrounds=64):
    lengths = [ord(i) for i in string] + _lengths
    vals = list(range(lsize))

    skip = 0
    index = 0

    for _round in range(_nrounds):
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

    # Now bitwise OR in chunks of 16 to get 16 bytes
    ord_chunks = [
        reduce(xor, vals[i:i+16])
        for i in range(0, 256, 16)
    ]
    binary = ''.join(
        '{:08b}'.format(i)
        for i in ord_chunks
    )
    return binary

print sum(
    sum(
        1 if char == '1' else 0
        for char in hash('{}-{}'.format(hash_key, i))
    )
    for i in range(128)
)
