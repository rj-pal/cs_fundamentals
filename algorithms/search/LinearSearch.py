def search(iterable, search_item):
    """
    Searches for a single item element in an iterable and returns its index. Calls find if 
    seach item is not a single element.

    Args:
        iterable (iterable): The iterable to search through any iterable object. 
        search_item (any single element): The item to search for in the iterable.

    Returns:
        int: The index of the first occurrence of `search_item` in `iterable`. 
             Returns -1 if the `search_item` is not found.
    """

    """
    Searches for an element or substring in an iterable and returns its index. Calls custom_find if 
    iterable is of type 'str'.

    Args:
        iterable (iterable): The iterable to search through. Can be any iterable object, including strings.
        search_item (any): The element or substring to search for in the iterable.

    Returns:
        int: The index of the first occurrence of `search_item` in `iterable`. 
             Returns -1 if the `search_item` is not found.

    Raises:
        ValueError: If `search_item` is empty (for strings).
        TypeError: If `iterable` is not an iterable object or if `search_item` is invalid.
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable.")
    print(search_item)
    if not search_item:
        raise ValueError("The 'search_item' must contain at least one element.")
    
    if isinstance(iterable, str):
        return custom_find(iterable, search_item)
    
    for i in range(len(iterable)):
        if iterable[i] == search_item:
            return i
    else:
        return -1
    
def custom_find(iterable, search_item):
    """
    Searches for a substring in a string and returns its starting index.

    Args:
        iterable (str): The string to search in.
        search_item (str): The substring to search for.

    Returns:
        int: The index of the first occurrence of `search_item` in `iterable`. 
             Returns -1 if `search_item` is not found.

    Raises:
        TypeError: If `iterable` is not a string.
    """
    if not isinstance(iterable, str):
        raise TypeError(f"'{type(iterable).__name__}' object is not of type 'str'.")
    
    if not search_item:
        raise ValueError("The 'search_item' must contain at least one element.")
    
    if len(search_item) > len(iterable):
        return -1
    
    for i in range(len(iterable) - len(search_item) + 1):
        if iterable[i] == search_item[0]:
            j = 0
            while j < len(search_item) and iterable[i + j] == search_item[j]:
                    j += 1
            else:
                return i
    else:
        return -1
    
# a=custom_find(["aaa", "bbb", "b", "b", "b"], "bbb")
# a = search('ontario', 'ntooooooooo')
# a = search(256,2)
# print(a)