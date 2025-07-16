def custom_sort(iterable: list) -> list:
    """
    In-place implementation of Bubble Sort algorithm with sorted back-of-list optimization and boolean flag for indicating no swaps and sorting completion.

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place).

    Raises:
        TypeError: If elements in the list are not comparable.
    """
    c = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(iterable) - 1 - c):
            try:
                if iterable[i] <= iterable[i+1]:
                    pass
                else:
                    iterable[i], iterable[i+1] = iterable[i+1], iterable[i]
                    swapped = True                 
            except TypeError as e:
                print('Traceback (most recent call last):')
                print('  File "algorithms/sorting/bubble_sort", line 10, in <module>')
                print(f'Type Error: {e}')
                raise TypeError
        c += 1      
    return iterable


def custom_sort_alternative(iterable: list) -> list:
    """
    In-place implementation of Bubble Sort algorithm with counter for indicating no swaps and sorting completion.

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place), or empty list if elements are not comparable.
    """
    c = 1
    while c != 0:
        c = 0
        for i in range(len(iterable) - 1):
            try:
                if iterable[i] <= iterable[i+1]:
                    pass
                else:
                    iterable[i], iterable[i+1] = iterable[i+1], iterable[i] 
            except TypeError as e:
                print(f'Type Error: {e}')
                return []   
    return iterable

def custom_sort_slow(iterable: list) -> list:
    """
    In-place implementation of an early break verion of Bubble Sort that exits loop early after one element position swap which adds extra compute time to sort.

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place), or empty list if elements are not comparable.
    """
    end = True
    while end:
        for i in range(len(iterable)-1):
            try:
                if iterable[i] <= iterable[i+1]:
                    pass
                else:
                    iterable[i], iterable[i+1] = iterable[i+1], iterable[i] 
                    break
            except TypeError as e:
                print(f'Type Error: {e}')
                return []
        else:
            end = False
    return iterable
