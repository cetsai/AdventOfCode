def main():
    total = 0
    with open("4/input") as f:
        for line in f:
            range1, range2 = line.rstrip().split(",")
            min1, max1 = [int(s) for s in range1.split("-")]
            min2, max2 = [int(s) for s in range2.split("-")]

            if (min1 <= min2 and max1 >= max2) or (min1 >= min2 and max1 <= max2):
                total += 1
    
    print(total)

if __name__ == "__main__":
    main()