def search(iterable, search_item):
    return binary_search(iterable, search_item, 0, len(iterable) - 1)


def binary_search(iterable, search_item, left, right):
    # print(f"Initial Left: {left}, Right: {right}")
    if left > right:
        return -1
    pointer = left + ((right - left) // 2)
    # print(f"Left: {left}, Right: {right}, Pointer {pointer}")
    if iterable[pointer] == search_item:
        # print("HERE")
        if pointer > 0 and iterable[pointer - 1] == search_item:
            return binary_search(iterable, search_item, left, pointer - 1)
        return pointer
    elif iterable[pointer] < search_item:
        return binary_search(iterable, search_item, pointer + 1, right)
    else:
        return binary_search(iterable, search_item, left, pointer - 1)
    