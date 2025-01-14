def search(iterable, search_item):
    for i in range(len(iterable)):
        if iterable[i] == search_item:
            return i
    else:
        return -1