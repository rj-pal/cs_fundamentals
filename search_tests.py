from util import custom_search
from algorithms.search import binary_search, linear_search

search_functions = [binary_search, linear_search]
sorted_list =[1,1,1,1,1,1,2,2,4,4,4,4,4,4,4]
expected_result=[-1, 0, 6, -1, 8, -1]
for search_function in search_functions:
    print(f"Testing {search_function.__name__}")
    for i in range(6):
        target = i
        expected_index = expected_result[i]
        result = custom_search(sorted_list, target, search_function)
        assert result == expected_index, f"Test Failed: Expected {expected_index}, got {result}"

print("All expected list tests passed!")

string = "nsfw"
c = 0
for letter in string:
    result = linear_search.search(string, letter)
    assert result == c, f"Test Failed: Expected {c}, got {result}"
    c += 1

print("String tests passed.")

c = 0
for letter in string:
    result = binary_search.search(string, letter)
    assert result == c, "Expected Test Failure with unsorted list."
    c += 1
