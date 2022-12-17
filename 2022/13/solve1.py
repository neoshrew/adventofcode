import json


INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"


def get_pairs():
    with open(INPUT_FNAME) as fandle:
        while True:
            left = json.loads(fandle.readline())
            right = json.loads(fandle.readline())
            yield left, right

            if not fandle.readline():
                break


def cmp(a, b):
    """
    if a < b -> 1
    if a == b -> 0
    if a > b -> -1
    """
    a_is_list = isinstance(a, list)
    b_is_list = isinstance(b, list)
    
    if not a_is_list and not b_is_list:
        if a > b:
            return 1
        elif a == b:
            return 0
        else: # a < b
            return -1

    if a_is_list and not b_is_list:
        b = [b]
    elif b_is_list and not a_is_list:
        a = [a]

    for a_item, b_item in zip(a, b):
        result = cmp(a_item, b_item)
        if result != 0:
            return result

    if len(a) > len(b):
        return 1
    elif len(a) == len(b):
        return 0
    else: # len(a) < len(b)
        return -1


def main():
    total = sum(
        index
        for index, (left, right) in enumerate(get_pairs(), 1)
        if cmp(left, right) == -1
    )
    print(total)






if __name__ == "__main__":
    main()