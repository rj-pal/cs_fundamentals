def custom_sort(iterable: list) -> list:
    """
    In-place implementation of Insertion Sort algorithm which inserts elements into correct position in sorted portion of the list with elements shifted to the right. 

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place).

    Raises:
        TypeError: If elements are not comparable.
    """
    for i in range(1, len(iterable)):
        key = iterable[i]
        print(key)
        for j in range(i, 0, -1):
            print(iterable)
            try:
                if key < iterable[j - 1]:
                    iterable[j] = iterable[j - 1]
                    print("ONE")
                    print(iterable)
                else:
                    iterable[j] = key
                    print("TWO")
                    print(iterable)
                    break
            except TypeError as e:
                print('Traceback (most recent call last):')
                print('  File "algorithms/sorting/insert_sort", line 6, in <module>')
                print(f'Type Error: {e}')
                raise TypeError
        else:
            print("here")
            iterable[0] = key
    return iterable

def custom_sort_slow(iterable: list) -> list:
    """
    In-place variant of Insertion Sort which uses a series of swaps to shift elements and place the current element into its sorted position within the preceding sub-list.

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place), or empty list if elements are not comparable.
    """
    for i in range(1, len(iterable)):
        for j in range(0, i):
            try:
                if iterable[i] < iterable[j]:
                    temp = iterable[i]
                    for k in range(j, i + 1):
                        iterable[k], temp = temp, iterable[k]
                    break
            except TypeError as e:
                print(f'Type Error: {e}')
                return []
    return iterable