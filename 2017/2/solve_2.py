with open('input.txt') as fandle:
    rows = [
        [int(cell) for cell in row.split()]
        for row in fandle
    ]


total = 0
for row in rows:
    this_row = sorted(row, reverse=True)
    for i, x in enumerate(this_row):
        for y in this_row[i+1:]:
            if x%y == 0:
                total += x/y
print total
