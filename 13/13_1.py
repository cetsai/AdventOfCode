import itertools as it

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
    """Returns -1 left comes before right, 1 if vice versa, 0 if equal"""
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
    
    return 0

def main():
    sum = 0
    with open("13/input") as f:
        iterators = [iter(f)] * 3
        for idx, (first, second, _) in enumerate(it.zip_longest(*iterators, fillvalue=""), start=1):
            left = parse_list(iter(first.removeprefix("[").rstrip()))
            right = parse_list(iter(second.removeprefix("[").rstrip()))
            sum += idx if compare_lists(left, right) == -1 else 0
    print(sum)

if __name__ == "__main__":
    main()