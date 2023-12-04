from collections import defaultdict

FNAME = "input.txt"
# FNAME = "test1.txt"


def get_cards():
    with open(FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if not line:
                continue

            # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            card_id_raw, all_numbers_raw = line.split(": ", 1)
            card_id = int(card_id_raw.split(" ")[-1])
            winning_numbers_raw, numbers_raw = all_numbers_raw.split(" | ")
            winning_numbers = [int(i) for i in winning_numbers_raw.split()]
            numbers = [int(i) for i in numbers_raw.split()]

            yield card_id, winning_numbers, numbers


def main():
    card_copies = defaultdict(int)
    for card_id, card_numbers, card_winning_numbers in get_cards():
        card_copies[card_id] += 1
        n_matches = len(set(card_numbers) & set(card_winning_numbers))
        for i in range(1, n_matches+1):
            card_copies[card_id+i] += card_copies[card_id]

    total = sum(card_copies.values())

    print(total)

if __name__ == "__main__":
    main()
