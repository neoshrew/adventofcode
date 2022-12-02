class ROCK: pass
class PAPER: pass
class SCISSORS: pass
LETTERS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}
ITEM_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
WIN_SCORES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0,
}

PAIR_WIN_SCORES = {
    (ROCK, ROCK): WIN_SCORES["DRAW"],
    (ROCK, PAPER): WIN_SCORES["WIN"],
    (ROCK, SCISSORS): WIN_SCORES["LOSE"],
    (PAPER, ROCK): WIN_SCORES["LOSE"],
    (PAPER, PAPER): WIN_SCORES["DRAW"],
    (PAPER, SCISSORS): WIN_SCORES["WIN"],
    (SCISSORS, ROCK): WIN_SCORES["WIN"],
    (SCISSORS, PAPER): WIN_SCORES["LOSE"],
    (SCISSORS, SCISSORS): WIN_SCORES["DRAW"],
}

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

def main():
    total = 0
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            if not line:
                continue
            pair = tuple(map(LETTERS.get, line.strip().split()))

            total += PAIR_WIN_SCORES[pair]
            total += ITEM_SCORES[pair[1]]

    print(total)

if __name__ == "__main__":
    main()
