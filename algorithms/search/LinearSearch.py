def search(iterable, search_element):
    """
    Searches for first occurance of given search element over iterable object using linear search algorithm. 
    
    Args:
        Iterable object (list)
        Element to be searched 
        
    Returns:
        Index of first occurance of search element, 0 for empty string; otherwise -1
            
    Raises:
        TypeError: If the iterable object is not iterable
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable.")
        
    if isinstance(iterable, str):
        return _linear_search_string(iterable, search_element)
    else:
        return _linear_search(iterable, search_element)

def _linear_search(iterable, search_element):
    """
    Internal linear search function for non-string iterables using brute force method.

    Args:d
        Iterable object (list, tuple, set, but not string)
        Element to be searched 
        
    Returns:
        Index of first occurance of search element, or -1 if not found.
    
    """ 
    for i in range(len(iterable)):
        if iterable[i] == search_element:
            return i
    return -1

def _linear_search_string(iterable, search_element):
    """
    Internal linear search function for string iterables using brute force method or niave algorithm.

    Args:
        Iterable object (str)
        Element to be searched (str)
        
    Returns:
        Index of first occurance of search element, 0 for empty search string, or -1 if not found.
            
    Raises:
        TypeError: If the iterable object is not a string
        TypeError: If the search element is not a string
    """
    if not isinstance(iterable, str):
        raise TypeError(f"'{type(iterable).__name__}' object is not of type 'str'.")
    
    if not isinstance(search_element, str):
        raise TypeError(f"'{type(search_element).__name__}' object is not of type 'str'.")
    
    if not search_element:
        return 0
    
    if len(search_element) > len(iterable):
        return -1
    
    for i in range(len(iterable) - len(search_element) + 1):
        if iterable[i] == search_element[0]:
            j = 0
            while j < len(search_element) and iterable[i + j] == search_element[j]:
                    j += 1
                    if j == len(search_element):
                        return i
    return -1
