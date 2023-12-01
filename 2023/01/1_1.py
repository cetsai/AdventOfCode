import re

def main():
    sum = 0
    with open("input") as f:
        for line in f:
            digits = list(map(int, re.findall(r"\d", line)))
            sum += (digits[0] * 10) + digits[-1]
            
    print(sum)


if __name__ == "__main__":
    main()