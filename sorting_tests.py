from util import custom_sorted
from algorithms.sorting import selection_sort, bubble_sort, insert_sort, merge_sort

import unittest

class TestSortFunction(unittest.TestCase):

    def setUp(self):
        """Set up the sort functions to test."""
        self.sort_functions = [selection_sort, insert_sort, bubble_sort, merge_sort]

    def test_empty_list(self):
        """Test sorting an empty list."""
        test_input_data = []
        expected_output = None
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_single_element(self):
        """Test sorting a list with a single element."""
        test_input_data = [42]
        expected_output = [42]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_sorted_list(self):
        """Test sorting an already sorted list."""
        test_input_data = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_unsorted_list(self):
        """Test sorting an unsorted list."""
        test_input_data = [15, 12, 9, 3, 6]
        expected_output = [3, 6, 9, 12, 15]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_duplicates(self):
        """Test sorting a list with multiple duplicate elements."""
        test_input_data = [24, 12, 24, 18, 12]
        expected_output = [12, 12, 18, 24, 24]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        test_input_data = [-3, -1, -4, -2, 0]
        expected_output = [-4, -3, -2, -1, 0]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_mixed_numbers(self):
        """Test sorting a list with both positive and negative numbers."""
        test_input_data = [-1, 1, 0, -2, 2]
        expected_output = [-2, -1, 0, 1, 2]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_string(self):
        """Test sorting a string."""
        test_input_data = "NSFW"
        expected_output = ["F", "N", "S", "W"]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_string_list(self):
        """Test sorting a list of strings."""
        test_input_data = ["apple", "cherry", "banana", "apple"]
        expected_output = ["apple", "apple", "banana", "cherry"]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_set(self):
        """Test sorting a set of strings."""
        test_input_data = {"apple", "banana", "cherry", "apple"}
        expected_output = ["apple", "banana", "cherry"]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
        # print("All Tests Cleared")

    def test_tuple(self):
        """Test sorting a tuple of strings."""
        test_input_data = ("apple", "banana", "cherry", "apple")
        expected_output = ["apple", "apple", "banana", "cherry"]
        for sort_function in self.sort_functions:
            # print(f"Test for {sort_function.__name__}")
            with self.subTest(sort_function=sort_function.__name__):        
                self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)

    def test_mixed_types(self):
        """Test sorting a list with mixed data types (should raise TypeError)."""
        test_input_data = [1, "one", 1.0]
        # expected_output = TypeError
        for sort_function in self.sort_functions:
            with self.subTest(sort_function=sort_function.__name__):
                # self.assertEqual(custom_sorted(test_input_data, sort_function), expected_output)
                with self.assertRaises(TypeError):
                    custom_sorted(test_input_data, sort_function)

if __name__ == "__main__":
    unittest.main()

exit()

# util.make_list(123)
print(custom_sorted([]))
print(custom_sorted([5,4,3]))
# exit()
# a = merge_sort.custom_sort("asdfsanlksdfuhaiuhasldkfnaslkdfj")
print(a)

print(custom_sorted([4,2,8,5,1,7,7,3]))
large_unsorted_list = [57, 23, 89, 1, 77, 34, 90, 21, 56, 78, 12, 3, 45, 67, 88, 92, 4, 39, 24, 70]
print(custom_sorted(large_unsorted_list))
# print(custom_sorted([5,4,3,2,1]))
# print(custom_sorted("bca"))
# print(custom_sorted(['a', 'b', 'c']))
print(sorted({4,2,8,5,1,7,7,3}))
# print(sorted((4,2,8,5,1,7,7,3)))
print(custom_sorted(2947))
print(custom_sorted([23,'3',4.5]))

# a = [2,3,4]
# b = ["r"]
# a.extend(5)
# b.extend("ter")
# a.extend(b)
# sorted(a)