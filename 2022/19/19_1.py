

def main():
    coordinates = []
    with open("testinput") as f:
        for line in f:
            coordinates.append(int(line))

    mixing_order = coordinates.copy()
    for i in mixing_order:
        pos = coordinates.index(i)
        new_pos = pos + i % len(coordinates)
        coordinates.pop(pos)
        coordinates.insert(new_pos, i)
        print(coordinates)


if __name__ == "__main__":
    main()
