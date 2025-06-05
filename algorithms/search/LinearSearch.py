def search(iterable, search_item):
    """
    Searches for first occurance of given search item over iterable object using linear search algorithm. Type checks for
    iterable object before performing the search using appropriate internal search algorithm.

    Returns the first the occurance of the search item, or 0 for empty string; otherwise -1 
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable.")
    
    if isinstance(iterable, str):
        return _linear_search_string(iterable, search_item)
    else:
        return _linear_search(iterable, search_item)

def _linear_search(iterable, search_item):
    """Internal linear search function for non-string iterables using brute force method."""    
    for i in range(len(iterable)):
        if iterable[i] == search_item:
            return i
    return -1

def _linear_search_string(iterable, search_item):
    """Internal linear search function for string iterables using brute force method.."""
    if not isinstance(iterable, str):
        raise TypeError(f"'{type(iterable).__name__}' object is not of type 'str'.")
    
    if not isinstance(search_item, str):
        raise TypeError(f"'{type(search_item).__name__}' object is not of type 'str'.")
    
    if not search_item:
        return 0
    
    if len(search_item) > len(iterable):
        return -1
    
    for i in range(len(iterable) - len(search_item) + 1):
        if iterable[i] == search_item[0]:
            j = 0
            while j < len(search_item) and iterable[i + j] == search_item[j]:
                    j += 1
                    if j == len(search_item):
                        return i
    return -1