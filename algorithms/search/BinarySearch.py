def search(iterable, search_item):
    """
    Searches for first occurance of given search item over sorted iterable object using binary search algorithm. 
    
    Args:
        Sorted iterable object (list)
        Element to be searched
    Returns:
        Index of first occurance of search element, 0 for empty string; otherwise -1
            
    Raises:
        TypeError: If the iterable object is not iterable
        TypeError: If the data type of the first item is not the same as the search item
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable.")
    
    if iterable:
        type_of_first_item = type(iterable[0])
        if not isinstance(search_item, type_of_first_item):
            raise TypeError(f"Search item type mismatch. Expected type '{type_of_first_item.__name__}', got '{type(search_item).__name__}' instead.")
        
    if isinstance(iterable, str):
        raise TypeError(f"'{type(iterable).__name__}' object is a single string iterable. Iterable should be an array-like object.")
    
    return _binary_search(iterable, search_item, 0, len(iterable) - 1)


def _binary_search(iterable, search_item, left, right):
    """
    Internal binary search function for sorted iterables using recursive method.
    
    Args:
        Sorted iterable object (list)
        Element to be searched
        Left index boundary for search range
        Right index boundary for search range
    
    Returns:
        Index of first occurance of search element, or -1 if not found.
    """
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

def _iterative_binary_search(iterable, search_item):
    """
    Internal binary search function for sorted iterables using iterative method.
    
    Args:
        Sorted iterable object (list)
        Element to be searched
    
    Returns:
        Index of first occurance of search element, or -1 if not found.
    """
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



    