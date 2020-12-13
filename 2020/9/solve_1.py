fname, preabmle_len = "input.txt", 25
# fname, preabmle_len = "test_input1.txt", 5

# being horrid, not eagerly closing fandle
numbers = (int(i) for i in open(fname))

# horridly assuming data won't end early
lookback = [next(numbers) for _ in range(preabmle_len)]

def validate(lookback, val):
    for ix, x in enumerate(lookback):
        for y in lookback[ix:]:
            if x+y == val:
                return True
    return False

for n in numbers:
    if not validate(lookback, n):
        break
    lookback.pop(0)
    lookback.append(n)

print(n)
