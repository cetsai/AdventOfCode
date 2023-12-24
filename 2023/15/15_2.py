import re


def ascii_code(string: str):
    result = 0
    for char in string:
        result = result + ord(char)
        result = result * 17 % 256
    return result


def main():
    steps: list[str]
    with open("input") as f:
        steps = f.readline().rstrip().split(',')
    boxes = [dict() for i in range(256)]
    for step in steps:
        match = re.fullmatch(r"(\D+)([-=])(\d*)", step)
        label, operation, focal_length = match.groups()
        box = boxes[ascii_code(label)]
        match operation:
            case '-':
                try:
                    del box[label]
                except KeyError:
                    continue
            case '=':
                box[label] = int(focal_length)
    result = 0
    for box_number, box in enumerate(boxes, start=1):
        for slot_number, focal_length in enumerate(box.values(), start=1):
            result += box_number * slot_number * focal_length
    print(result)


if __name__ == "__main__":
    main()
