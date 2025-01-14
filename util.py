def custom_sorted(iterable, sort_function):
    data = make_list(iterable)
    if not data:
        return None
    return sort_function.custom_sort(data)

def custom_search(iterable, search_item, search_function):
    data = make_list(iterable)
    if not data:
        return None
    return search_function.search(data, search_item)

def make_list(iterable):
    try:
        iterable = list(iterable)
    except TypeError as e:
        print(f'TypeError: {e}')
        return
    return iterable 

def insert_custom(iterable, index, object):
    iterable = make_list(iterable)
    temp_var = object
    for i in range(index, len(iterable)):
        iterable[i], temp_var = temp_var, iterable[i]
    return iterable + [temp_var]
# print(insert_custom([1,2,3,4,5], 2, "g"))
# print(insert("I want u", 29, "U"))
# print(make_list(True))