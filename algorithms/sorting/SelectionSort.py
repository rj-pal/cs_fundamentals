import traceback

def custom_sort(iterable: list) -> list:
    """
    In-place implementation of Selection Sort , which finds the minimum element from the unsorted part of the list and swaps it with the element at the current beginning of the unsorted part.


    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place).

    Raises:
        TypeError: If elements are not comparable. A custom traceback message is printed to the console before the exception is re-raised.
    """
    for i in range(len(iterable)):
        min_index = i
        for j in range(i + 1, len(iterable)):
            try:
                if iterable[j] < iterable[min_index]:
                    min_index = j
            except TypeError as e:
                print('Traceback (most recent call last):')
                print('  File "algorithms/sorting/selecdtion_sort", line 9, in <module>')
                print(f'Type Error: {e}')
                raise TypeError
        iterable[min_index], iterable[i] = iterable[i], iterable[min_index]

    return iterable

def custom_sort_alt(iterable: list) -> list:
    """
    In-place implementation of Selection Sort, which finds the minimum element from the unsorted part of the list and swaps it with the element at the current beginning of the unsorted part.

    Args:
        iterable: The list to be sorted.

    Returns:
        The sorted list (modified in-place), or returns `None` if a TypeError occurs during comparison.
    """
    j = len(iterable)            
    i = 0
    while i < j:
        min_index = i
        for n in range(i + 1, j):
            try:
                if iterable[n] < iterable[min_index]:
                    min_index = n
            except TypeError as e:
                print(traceback.format_exc(limit=0))
                return
        iterable[min_index], iterable[i] = iterable[i], iterable[min_index]
        i += 1

    return iterable
