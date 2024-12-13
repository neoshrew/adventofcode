FNAME = "input.txt"
# FNAME = "test1.txt"

def get_stones():
    with open(FNAME) as fandle:
        return [
            int(i)
            for i in fandle.read().split()
        ]


CACHE = {}
def get_stone_count(stone_n, generations):
    if generations == 0:
        return 1

    if (stone_n, generations) in CACHE:
        return CACHE[stone_n, generations]

    result = _get_stone_count(stone_n, generations)
    CACHE[stone_n, generations] = result

    return result


def _get_stone_count(stone_n, generations):
    if stone_n == 0:
        return get_stone_count(1, generations-1)

    
    stone_str = str(stone_n)
    digits = len(stone_str)
    if digits %2 == 0:
        half = digits // 2
        return (
            get_stone_count(int(stone_str[:half]), generations-1)
            + get_stone_count(int(stone_str[half:]), generations-1)
        )

    return get_stone_count(stone_n*2024,generations-1)


def main():
    stones = get_stones()

    generations = 75

    total = sum(
        get_stone_count(stone_n, generations)
        for stone_n in stones
    )

    print(total)


if __name__ == "__main__":
    main()