with open('input.txt') as fandle:
    print sum(
        max(row) - min(row)
        for row in (
            [int(cell) for cell in row.split()]
            for row in fandle
        )
    )