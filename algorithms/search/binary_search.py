
def search(iterable, search_item, left, right):
    print(f"Initial Left: {left}, Right: {right}")
    if left > right:
        return -1
    pointer = left + ((right - left) // 2)
    print(f"Left: {left}, Right: {right}, Pointer {pointer}")
    if iterable[pointer] == search_item:
        print("HERE")
        if pointer > 0 and iterable[pointer - 1] == search_item:
            return search(iterable, search_item, left, pointer - 1)
        return pointer
    elif iterable[pointer] < search_item:
        return search(iterable, search_item, pointer + 1, right)
    else:
        return search(iterable, search_item, left, pointer - 1)

# b=[1,1,1,1,1,1,2,2,4,4,4,4,4,4,4]
# c=len(b)-1
# for i in range(6):
#     a=search(b, i, 0, c)
#     print(a)