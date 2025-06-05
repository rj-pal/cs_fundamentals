def search(iterable, search_item):
    """
    Searches for first occurance of given search item over sorted iterable object using binary search algorithm. Type checks 
    for iterable object before performing the search using interal binary search algorithm.

    Returns the first the occurance of the search item; otherwise -1.
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable.")
    
    if iterable:
        type_of_first_item = type(iterable[0])
        if not isinstance(search_item, type_of_first_item):
            raise TypeError(f"Search item type mismatch. Expected type '{type_of_first_item.__name__}', got '{type(search_item).__name__}' instead.")
    
    return iterative_binary_search(iterable, search_item)
    # return _binary_search(iterable, search_item, 0, len(iterable) - 1)


def _binary_search(iterable, search_item, left, right):
    """Internal binary search function for iterables using recursive method."""
    if left > right:
        return -1
    pointer = left + ((right - left) // 2)
    if iterable[pointer] == search_item:
        if pointer > 0 and iterable[pointer - 1] == search_item:
            return _binary_search(iterable, search_item, left, pointer - 1)
        return pointer
    elif iterable[pointer] < search_item:
        return _binary_search(iterable, search_item, pointer + 1, right)
    else:
        return _binary_search(iterable, search_item, left, pointer - 1)

def iterative_binary_search(iterable, search_item):
    left = 0
    right = len(iterable) - 1
    result = -1
    while left <= right:
        pointer = left + ((right - left) // 2)
        if iterable[pointer] == search_item:
            result = pointer
            if pointer > 0 and iterable[pointer - 1] == search_item:
                right  = pointer - 1
            else:
                return pointer         
        elif iterable[pointer] < search_item:
            left = pointer + 1
        else:
            right = pointer - 1
    
    return result

# Might be flaw in logic
def iterative_binary_search_alt(iterable, search_item):
    left = 0
    right = len(iterable) - 1
    while left <= right:
        pointer = left + ((right - left) // 2)
        if iterable[pointer] == search_item:
            if pointer > 0 and iterable[pointer - 1] == search_item:
                left = pointer - 2
                right  = pointer
            else:
                return pointer         
        elif iterable[pointer] < search_item:
            left = pointer + 1
        else:
            right = pointer - 1   
    return -1

print(search([1,2,3,4,5,6,7,8], 4))
print(search([1,2,3,4,5,6,7,8], 14))
print(search([1,2,3,4,5,6,7,8,9,9,9,10,12], 9))
print(search([1,2,3], 3))



    