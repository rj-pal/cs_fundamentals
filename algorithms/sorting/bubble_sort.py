def custom_sort(iterable):
    c = 0
    swapped = True
    # n=0
    while swapped:
        swapped = not swapped
        for i in range(len(iterable) - 1 - c):
            # n += 1
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
    # print(n)
    return iterable


def custom_sort_alt(iterable):
    end = True
    n = 0
    while end:
        for i in range(len(iterable)-1):
            n += 1
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
    print(n)
    return iterable

def custom_sort_alt2(iterable):
    c = 1
    n = 0
    while c != 0:
        c = 0
        n+=1
        for i in range(len(iterable)-1):
            n+=1
            try:
                if iterable[i] <= iterable[i+1]:
                    pass
                else:
                    iterable[i], iterable[i+1] = iterable[i+1], iterable[i] 
                    c += 1
            except TypeError as e:
                print(f'Type Error: {e}')
                return []   
    print(n)
    return iterable
