fname = "input.txt"

TESTS = [
    ("1 + 2 * 3 + 4 * 5 + 6", 231),
    ("2 * 3 + (4 * 5)", 46),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
]

TOKENDICT = dict([
    *zip("+*()", "+*()"),
    *zip("0123456789", range(10)),
])

def get_next(list_, item, start):
    try:
        return list_.index(item, start)
    except ValueError:
        return None


def tokenize(raw_sum):
    # Looking at the input we only ever have single digit numbers.
    return [
        TOKENDICT[c] for c in raw_sum if c in TOKENDICT
    ]

def evaluate_sum(raw_sum):
    tokens = tokenize(raw_sum)
    return _evaluate_sum(tokens)

def _evaluate_sum(tokens):
    start = 0
    while (pair := _get_bracket_pairs(tokens, start)) is not None:
        pair_l, pair_r = pair
        tokens[pair_l:pair_r+1] = [_evaluate_sum(tokens[pair_l+1:pair_r])]

    _sums(tokens, '+', lambda x, y: x+y)
    _sums(tokens, '*', lambda x, y: x*y)

    return tokens[0]

def _get_bracket_pairs(tokens, start):
    if (start := get_next(tokens, '(', start)) is None:
        return None
    pair_l = start
    start += 1
    count = 0
    while True:
        n = min(
            get_next(tokens, '(', start) or len(tokens),
            get_next(tokens, ')', start),
        )
        start = n+1

        if tokens[n] == '(':
            count += 1
        else: # tokens[n] == ')'
            if count == 0:
                return pair_l, n
            else:
                count -= 1


def _sums(tokens, c, op):
    i = 0
    while True:
        if (i := get_next(tokens, c, i)) is None:
            break
        tokens[i-1:i+2] = [op(tokens[i-1], tokens[i+1])]


if False:
    for test_raw, expected_result in TESTS:
        actual_result = evaluate_sum(test_raw)
        print(
            actual_result == expected_result,
            actual_result,
            expected_result,
            test_raw,
        )
        if actual_result != expected_result:
            print("ERROR")
            break

total = 0
with open(fname) as fandle:
    for line in fandle:
        line = line.rstrip()
        total += evaluate_sum(line)

print(total)
