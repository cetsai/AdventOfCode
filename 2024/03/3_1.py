import re

def main():
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = []
    with open("input") as f:
        for line in f:
            matches.extend(re.findall(pattern, line))
    
    sum = 0
    for a, b in matches:
        sum += int(a) * int(b)

    print(sum)
            


if __name__ == "__main__":
    main()