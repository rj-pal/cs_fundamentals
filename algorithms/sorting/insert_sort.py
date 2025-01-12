def custom_sort(iterable):
    for i in range(1, len(iterable)):
        key = iterable[i]
        for j in range(i, 0, -1):
            try:
                if key < iterable[j-1]:
                    iterable[j] = iterable[j-1]
                else:
                    iterable[j] = key
                    break
            except TypeError as e:
                print('Traceback (most recent call last):')
                print('  File "algorithms/sorting/insert_sort", line 6, in <module>')
                print(f'Type Error: {e}')
                return TypeError
        else:
            iterable[0] = key
    return iterable

def custom_sort_alt(iterable):
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