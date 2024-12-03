import re

def main():
    pattern = re.compile(r"(?:mul\((\d{1,3}),(\d{1,3})\))|"
                         r"(?P<do>do\(\))|"
                         r"(?P<dont>don't\(\))")
    matches = []
    with open("input") as f:
        for line in f:
            matches.extend(re.finditer(pattern, line))
    
    sum = 0
    enabled = True
    for m in matches:
        if m["do"]:
            enabled = True
        elif m["dont"]:
            enabled = False
        else:
            sum += 0 if not enabled else int(m[1]) * int(m[2])
    
    print(sum)
            


if __name__ == "__main__":
    main()