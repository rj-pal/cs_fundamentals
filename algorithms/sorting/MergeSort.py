
def merge_sorted_arrays(left, right):
    merged_array = [None] * (len(left) + len(right))
    pointer_left, pointer_right, merge_index = 0, 0, 0
    # Merge until one of the arrays is exhausted
    try:
        while pointer_left < len(left) and pointer_right < len(right):
            if left[pointer_left] <= right[pointer_right]:
                merged_array[merge_index] = left[pointer_left]
                pointer_left += 1
            else:
                merged_array[merge_index] = right[pointer_right]
                pointer_right += 1
            merge_index += 1
    except TypeError as e:
        print('Traceback (most recent call last):')
        print('  File "algorithms/sorting/merge_sort", line 9, in <module>')
        print(f'Type Error: {e}')
        raise TypeError
    while pointer_left < len(left):
        merged_array[merge_index] = left[pointer_left]
        pointer_left += 1
        merge_index += 1  
    while pointer_right < len(right):
        merged_array[merge_index] = right[pointer_right]
        pointer_right += 1
        merge_index += 1     
    return merged_array

def custom_merge(iterable, start, end):
    if end - start  <= 1:
        return iterable[start:end]
    mid_point = (start + end) // 2
    left = custom_merge(iterable, start, mid_point)
    right = custom_merge(iterable, mid_point, end)
    
    return merge_sorted_arrays(left, right)

def custom_sort(iterable):
    return custom_merge(iterable, 0, len(iterable))

# INPLACE MERGE SORT
# def merge_sorted_arrays(iterable, start, mid, end, temp):
#     # Use pointers for left and right subarrays
#     pointer_left, pointer_right = start, mid
#     merge_index = start

#     # Merge until one of the arrays is exhausted
#     while pointer_left < mid and pointer_right < end:
#         if iterable[pointer_left] <= iterable[pointer_right]:
#             temp[merge_index] = iterable[pointer_left]
#             pointer_left += 1
#         else:
#             temp[merge_index] = iterable[pointer_right]
#             pointer_right += 1
#         merge_index += 1

#     # Copy any remaining elements from the left subarray
#     while pointer_left < mid:
#         temp[merge_index] = iterable[pointer_left]
#         pointer_left += 1
#         merge_index += 1

#     # Copy any remaining elements from the right subarray
#     while pointer_right < end:
#         temp[merge_index] = iterable[pointer_right]
#         pointer_right += 1
#         merge_index += 1

#     # Copy merged elements back to the original array
#     for i in range(start, end):
#         iterable[i] = temp[i]


# def custom_merge(iterable, start, end, temp):
#     if end - start <= 1:  # Base case: single element or empty sublist
#         return

#     # Find the midpoint
#     mid_point = (start + end) // 2

#     # Recursively sort the left and right halves
#     custom_merge(iterable, start, mid_point, temp)
#     custom_merge(iterable, mid_point, end, temp)

#     # Merge the sorted halves
#     merge_sorted_arrays(iterable, start, mid_point, end, temp)


# def custom_sort(iterable):
#     if not isinstance(iterable, list):
#         raise ValueError("Input must be a list.")

#     # Create a temporary array for merging
#     temp = [0] * len(iterable)

#     # Perform merge sort
#     custom_merge(iterable, 0, len(iterable), temp)

#     return iterable

# print(merge_sorted_arrays([1,3,5,7,9],[2,4,6,8,10,12,14,16,18]))
# print(merge_sorted_arrays([5], [3]))
# print(merge_sorted_arrays([], []))  # Output: []
# print(merge_sorted_arrays([1, 2, 3], []))  # Output: [1, 2, 3]
# print(merge_sorted_arrays([], [4, 5, 5, 6, "seven"]))  # Output: [4, 5, 6]
# print(custom_sort([1, "one", 1.0]))

# print(custom_sort([3,6,3,56,3,6,3,7,]))
# print(custom_sort([8,26,8,12,49,32,3,6,76,35]))

# print(custom_sort([]))
# print(custom_sort([2,3]))
# print(custom_sort([8,3]))
# print(custom_sort(["three",2]))
# print(custom_sort([8,26,8,12,49,32,3,6,76,35,"d"]))
# print(custom_sort([1,2,3,4,5]))

# exit()