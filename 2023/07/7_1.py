

def hand_cmp(left: Hand, right: Hand) -> int:
    return 0


def main():
    hands = []
    with open("testinput") as f:
        for line in f:
            cards, bid = line.split()
            counts = {}
            for card in cards:
                if card in counts:
                    counts[card] += 1
                else:
                    counts[card] = 1
            hands.append((cards, int(bid), counts))
        print(hands)


if __name__ == "__main__":
    main()
