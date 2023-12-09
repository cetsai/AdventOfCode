"""
https://adventofcode.com/2023/day/7

Each line of the input is a hand of cards and a bid. The task is to
rank the hands and for each hand multiply the bid by the rank to obtain
its score. The final answer is the sum of these scores.

The main difficulty of the problem comes from choosing how to represent
hands and define their ranking in code. I chose to store the hand type
as an enum that is assigned when the Hand is created, which makes the
comparison relatively straightforward.
"""
from __future__ import annotations
from functools import total_ordering, cache
from dataclasses import dataclass, field
from enum import IntEnum


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


@total_ordering
@dataclass
class Hand:
    cards: str
    bid: int
    type: HandType = field(init=False, compare=False)

    def __post_init__(self):
        counts = {}
        for card in self.cards:
            if card in counts:
                counts[card] += 1
            else:
                counts[card] = 1
        groups = sorted(list(counts.items()), key=lambda x: x[1], reverse=True)
        match groups:
            case [tuple((_, 5))]:
                self.type = HandType.FIVE_KIND
            case [tuple((_, 4)), _]:
                self.type = HandType.FOUR_KIND
            case [tuple((_, 3)), tuple((_, 2))]:
                self.type = HandType.FULL_HOUSE
            case [tuple((_, 3)), _, _]:
                self.type = HandType.THREE_KIND
            case [tuple((_, 2)), tuple((_, 2)), _]:
                self.type = HandType.TWO_PAIR
            case [tuple((_, 2)), _, _, _]:
                self.type = HandType.ONE_PAIR
            case [*_]:
                self.type = HandType.HIGH_CARD

    def __lt__(self, other: Hand):
        if self.type != other.type:
            return self.type < other.type
        for left, right in zip(self.cards, other.cards):
            if left != right:
                return Hand.card_value(left) < Hand.card_value(right)
        return False
    
    @cache
    @staticmethod
    def card_value(card: str):
        values = ['2', '3', '4', '5', '6', '7', '8', '9',
                  'T', 'J', 'Q', 'K', 'A']
        return values.index(card)


def main():
    hands:list[Hand] = []
    card_ranks = []
    with open("input") as f:
        for line in f:
            cards, bid = line.split()
            hands.append(Hand(cards, int(bid)))
    
    result = 0
    for i, hand in enumerate(sorted(hands)):
        result += (i + 1) * hand.bid
    print(result)


if __name__ == "__main__":
    main()
