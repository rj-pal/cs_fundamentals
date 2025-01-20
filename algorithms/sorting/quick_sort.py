# Niave partition
def partition(iterable, pivot):
    left = []
    right = []
    pivot_point = iterable[pivot]
    for i in iterable[:pivot]:
        if i < pivot_point:
            left.append(i)
        else:
            right.append(i)
    for i in iterable[pivot+1:]:
        if i < pivot_point:
            left.append(i)
        else:
            right.append(i)

    return left, right

def test_partition(iterable):
    pivot_index = len(iterable) // 2
    pivot_value = iterable[pivot_index]
    print(f"Pivot Value: {pivot_value}")
    i, j = 0, len(iterable) - 1
    while i != j:
        if iterable[i] < pivot_value:
            i += 1
        else:
            if iterable[j] > pivot_value:
                j -= 1
            elif iterable[i] == iterable[j]:
                i += 1
                j += 1
            else:
                iterable[i], iterable[j] = iterable[j], iterable[i]
    iterable[i] = pivot_value
    return iterable

def custom_sort(iterable):
    if len(iterable) <= 1:
        return iterable
    pivot = len(iterable)//2
    left, right = partition(iterable, pivot)
    pivot_value = iterable[pivot]
    return custom_sort(left) + [pivot_value] + custom_sort(right)

# print(partition([8, 2, 3, 2, 2, 1]))
# print(partition([2,5,16,6,19,9,1,25,35,4,5]))
# print(partition([12,4]))
# print(partition([4,4,4,4,4,4]))

# print(custom_sort([3,6,3,56,3,6,3,7,]))
# print(custom_sort([8,26,8,12,49,32,3,6,76,35]))
# print(custom_sort([4,4,4,4,4,4]))


# print(custom_sort([3]))
# print(custom_sort([2,3]))
# print(custom_sort([3,2]))
# print(custom_sort([8,26,8,12,49,32,3,6,76,35]))
