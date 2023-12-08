from collections import Counter

FNAME = "input.txt"
# FNAME = "test1.txt"

class Card:
    card_values = {
        k: v
        for v, k in enumerate("J23456789TQKA")
    }
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<{}: {}>".format(
            self.__class__.__name__,
            self.value
        )

    @property
    def n_value(self):
        return self.card_values[self.value]

    def __lt__(self, other):
        return self.n_value < other.n_value

    def __eq__(self, other):
        return self.n_value == other.n_value


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __lt__(self, other):
        self_type = self.get_hand_type()[1]
        other_type = other.get_hand_type()[1]
        if self_type < other_type:
            return True
        if self_type > other_type:
            return False
        return self.cards < other.cards

    def get_hand_type(self):
        cards = list(card.value for card in self.cards)
        card_set = set(cards)
        if "J" not in card_set or card_set == {"J"}:
            return self._get_hand_type(cards)

        card_set.remove("J")
        curr = "", 0
        for new_card in card_set:
            new_cards = cards[::]
            for i in range(len(new_cards)):
                if new_cards[i] == "J":
                    new_cards[i] = new_card
            potential = self._get_hand_type(new_cards)
            if potential[1] > curr[1]:
                curr = potential
        return curr


    @staticmethod
    def _get_hand_type(cards):
        # AoC have been quite kind with the hands, and we can analyse them all
        # as disctinct counts, rather than checking for runs (e.g. a straight)
        # and we have no suits to worry about (e.g. a flush)
        counts = sorted(Counter(cards).values())

        # Five of a kind, where all five cards have the same label: AAAAA
        if counts == [5]:
            return "Five-of-a-kind", 7
        # Four of a kind, where four cards have the same label and one card
        # has a different label: AA8AA
        if counts == [1, 4]:
            return "Four-of-a-kind", 6
        # Full house, where three cards have the same label, and the remaining
        # two cards share a different label: 23332
        if counts == [2, 3]:
            return "Full-house", 5
        # Three of a kind, where three cards have the same label, and the
        # remaining two cards are each different from any other card in the hand: TTT98
        if counts == [1, 1, 3]:
            return "Three-of-a-kind", 4
        # Two pair, where two cards share one label, two other cards share a
        # second label, and the remaining card has a third label: 23432
        if counts == [1, 2, 2]:
            return "Two-pair", 3
        # One pair, where two cards share one label, and the other three cards
        # have a different label from the pair and each other: A23A4
        if counts == [1, 1, 1, 2]:
            return "Pair", 2

        # High card, where all cards' labels are distinct: 23456
        return "High-card", 1


    @classmethod
    def from_str(cls, raw_string):
        raw_cards, raw_bid = raw_string.split()

        return cls(
            [Card(i) for i in raw_cards],
            int(raw_bid),
        )

    def __repr__(self):
        return "<{}: {} {} {} >".format(
            self.__class__.__name__,
            "".join(card.value for card in self.cards),
            self.get_hand_type()[0],
            self.bid,
        )

def get_hands():
    with open(FNAME) as fandle:
        return [
            Hand.from_str(line)
            for line in fandle
            if line.strip()
        ]


def main():
    hands = get_hands()

    total = 0
    for rank, hand in enumerate(sorted(hands), 1):
        total += rank * hand.bid

    print(total)

if __name__ == "__main__":
    main()

# 765 * 1
# 220 * 2
# 28 * 3
# 684 * 4
# 483 * 5
#
