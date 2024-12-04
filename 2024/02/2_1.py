from itertools import pairwise

def isReportSafe(report: list[int]) -> bool:
    if len(report) < 2:
        return True
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