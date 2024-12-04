from itertools import pairwise
from functools import reduce

def isReportSafe(report: list[int]) -> bool:
    if len(report) < 2:
        return True
    diffs = [b - a for a, b in pairwise(report)]
    signs = [a * b for a, b in pairwise(diffs)]
    if reduce(signs, lambda x, y: x + 1 if y > 0 else x) > 1:
        return False
    sign = report[1] - report[0]
    for a, b in pairwise(report):
        diff = b - a
        if diff * sign <= 0:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True

def main():
    reports = []
    with open("input") as f:
        for line in f:
            reports.append(list(map(int, line.split())))
        
    print(sum(map(isReportSafe, reports)))

if __name__ == "__main__":
    main()