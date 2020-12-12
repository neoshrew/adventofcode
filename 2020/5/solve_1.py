# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

fname = "input.txt"
# fname = "test_input1.txt"

def get_bvec_deets(bvec):
    for replacement in ("F0", "B1", "L0", "R1"):
        bvec = bvec.replace(*replacement)

    seat_id = int(bvec, 2)
    row = seat_id // 8
    column = seat_id % 8
    return seat_id, row, column


with open(fname) as fandle:
    print(max(
        get_bvec_deets(line.rstrip())[0]
        for line in fandle
    ))
