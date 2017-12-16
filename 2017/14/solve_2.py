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
        reduce(xor, vals[chunk_i:chunk_i+16])
        for chunk_i in range(0, 256, 16)
    ]
    binary = ''.join(
        '{:08b}'.format(i)
        for i in ord_chunks
    )
    return binary


grid = [
    [
        char == '1'
        for char in hash('{}-{}'.format(hash_key, i))
    ]
    for i in range(128)
]


to_visit = set(
    (x, y)
    for x in range(128)
    for y in range(128)
    if grid[x][y]
)


_MODS = ((-1, 0), (1, 0), (0, -1), (0, 1))
def get_surrounding_coords((x, y)):
    for i, j in _MODS:
        coord = (x+i, y+j)
        if coord in to_visit:
            to_visit.remove(coord)
            yield coord


total_sectors = 0

while to_visit:
    total_sectors += 1
    this_sector = [to_visit.pop()]
    while this_sector:
        # There's no need to actuall number the cells with their sector,
        # just find all the ones in the current sector and remove them
        # from our set of blocks.
        curr = this_sector.pop()
        this_sector.extend(get_surrounding_coords(curr))

print total_sectors
