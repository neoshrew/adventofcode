fname, preabmle_len = "input.txt", 25
# fname, preabmle_len = "test_input1.txt", 5


with open(fname) as fandle:
    numbers = [int(i) for i in fandle]

# horridly assuming data won't end early
lookback = numbers[:preabmle_len]

def validate(lookback, val):
    for ix, x in enumerate(lookback):
        for y in lookback[ix:]:
            if x+y == val:
                return True
    return False

for first_inval in numbers[preabmle_len:]:
    if not validate(lookback, first_inval):
        break
    lookback.pop(0)
    lookback.append(first_inval)

total = lp = rp = 0
while total != first_inval:
    if total < first_inval:
        total += numbers[rp]
        rp += 1
    else:
        total -= numbers[lp]
        lp += 1

xmas_weakness = min(numbers[lp:rp]) + max(numbers[lp:rp])
print(xmas_weakness)
