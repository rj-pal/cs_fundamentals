
import traceback

def custom_sort(iterable):
    for i in range(len(iterable)):
        min_index = i
        for j in range(i+1,len(iterable)):
            try:
                if iterable[j] < iterable[min_index]:
                    min_index = j
            except TypeError as e:
                print('Traceback (most recent call last):')
                print('  File "algorithms/sorting/selecdtion_sort", line 9, in <module>')
                print(f'Type Error: {e}')
                return TypeError
        iterable[min_index], iterable[i] = iterable[i], iterable[min_index]

    return iterable


def custom_sort_alt(iterable):
    j = len(iterable)            
    i = 0
    while i < j:
        min_val = iterable[i]
        min_index = i
        for n in range(i+1, j):
            try:
                if iterable[n] < min_val:
                    min_val = iterable[n]
                    min_index = n
            except TypeError as e:
                print(traceback.format_exc(limit=0))
                return
        iterable[min_index], iterable[i] = iterable[i], min_val
        i += 1

    return iterable
