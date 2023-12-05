"""
In part 2, instead of receiving a score for matching numbers, you
instead get copies of the next N cards (N is the number of matches).
The task is to find how many cards you have at the end.

Since each card's count depends only on the previous cards, this can be
done in a single pass. Keep a queue of upcoming card counts and when
additional copies are won, add them to the corresponding queue entry.
On each card, pop the first element of the queue and add to the result.
If the queue is empty, default to a count of 1 (the original copy).
"""
import re


def main():
    result = 0
    card_counts = []
    with open("input") as f:
        for line in f:
            colon_index = line.find(':')
            bar_index = line.find('|')
            winning_numbers = re.findall(r"\d+", line[colon_index:bar_index])
            candidate_numbers = re.findall(r"\d+", line[bar_index:])
            scoring_numbers = set(winning_numbers) & set(candidate_numbers)
            current_card_count = card_counts.pop(0) if card_counts else 1
            card_counts.extend([1] * (len(scoring_numbers) - len(card_counts)))
            for i in range(len(scoring_numbers)):
                card_counts[i] += current_card_count
            result += current_card_count
    print(result)


if __name__ == "__main__":
    main()