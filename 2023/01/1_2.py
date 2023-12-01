import re

def main():
    # keeping first and last letters as a small hack to handle cases like "twone"
    digit_map = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    sum = 0

    with open("input") as f:
        for line in f:
            for old, new in digit_map.items():
               line = line.replace(old, new)
            digits = list(map(int, re.findall(r"\d", line)))
            sum += (digits[0] * 10) + digits[-1]
            
    print(sum)


if __name__ == "__main__":
    main()