import itertools as it
from functools import cmp_to_key

def parse_list(str_iter):
    result_list = []
    current_element = ""
    for char in str_iter:
        if char == "[":
            result_list.append(parse_list(str_iter))
            continue
        if char.isdigit():
            current_element += char
            continue
        if current_element:
            result_list.append(int(current_element))
            current_element = ""
        if char == "]":
            return result_list
        
def compare_lists(left_list, right_list):
    """Returns -1 if left < right, 1 if left > right, 0 if equal"""
    for left_item, right_item in it.zip_longest(left_list, right_list, fillvalue=None):
        if left_item is None:
            return -1
        if right_item is None:
            return 1
        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item < right_item:
                return -1
            elif left_item > right_item:
                return 1
            else:
                continue

        left_item = left_item if isinstance(left_item, list) else [left_item]
        right_item = right_item if isinstance(right_item, list) else [right_item]
        res = compare_lists(left_item, right_item)
        if compare_lists(left_item, right_item):
            return res

def main():
    packets = [[[2]], [[6]]]
    with open("13/input") as f:
        for line in map(str.rstrip, f):
            if not line:
                continue
            packet = parse_list(iter(line.removeprefix("[")))
            packets.append(packet)

    packets = sorted(packets, key=cmp_to_key(compare_lists))
    idx1 = packets.index([[2]]) + 1
    idx2 = packets.index([[6]]) + 1
    print(idx1 * idx2)
    

if __name__ == "__main__":
    main()