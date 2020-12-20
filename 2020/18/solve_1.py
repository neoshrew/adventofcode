fname = "input.txt"

TESTS = [
    ("1 + 2 * 3 + 4 * 5 + 6", 71),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 26),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]


def tokenize(raw_sum):
    # Looking at the input we only ever have single digit numbers.
    return [c for c in raw_sum if c != ' ']

def evaluate_sum(raw_sum):
    components = tokenize(raw_sum)
    stack = []
    curr_val, curr_op = None, None

    for component in components:
        if component in "1234567890":
            component = int(component)

            if curr_val is None:
                curr_val = component

            else:
                if curr_op == '*':
                    curr_val *= component
                else: # curr_op == '+':
                    curr_val += component
                curr_op = None

        elif component in "+*":
            curr_op = component

        elif component == '(':
            stack.append((curr_val, curr_op))
            curr_val, curr_op = None, None

        elif component == ')':
            old_val, old_op = stack.pop()

            if old_op is None:
                if old_val is not None:
                    curr_val = old_val
            elif old_op == '*':
                curr_val *= old_val
            else: # old_op == '+':
                curr_val += old_val
            curr_op = None


    return curr_val

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
