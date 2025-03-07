from typing import List

def sort(param: List[int]) -> List[int]:
    """
    A recursive implementation of the QuickSort algorithm.

    Time Complexity:
        - Best/Average Case: O(n log n)
        - Worst Case: O(n^2) (when the pivot selection is poor, e.g., always selecting the smallest or largest element)

    Space Complexity:
        - O(n) (due to the recursive call stack and extra lists used for partitioning)

    :param param: A list of integers to be sorted.
    :return: A sorted list in ascending order.
    """

    # Base case: If the list has one or no elements,
    # return it as is (already sorted).
    if len(param) <= 1:
        return param
    else:
        # Get the length of the list
        length = len(param)

        # Choose the middle element as the pivot
        pivot = length // 2

        # List to store elements smaller than or equal to the pivot
        left = []

        # List to store elements greater than the pivot
        right = []

        # Iterate through the list and partition elements
        # into left and right sublists
        for index, value in enumerate(param):
            # Skip the pivot element itself
            if index != pivot:
                if value <= param[pivot]:
                    # Add to left if value is smaller or equal to pivot
                    left.append(value)
                else:
                    # Add to right if value is greater than pivot
                    right.append(value)

        # Recursively sort left and right sublists,
        # then concatenate them with the pivot
        return sort(left) + [param[pivot]] + sort(right)

# Test cases

# Test case 1: Regular unsorted list
test1 = [1, 2, 3, 2, 2, -11, 223]
print("Test 1 - Sorted List:", sort(test1))

# Test case 2: List with only one element (already sorted)
test2 = [42]
print("Test 2 - Sorted List:", sort(test2))

# Test case 3: List with all identical elements
test3 = [7, 7, 7, 7, 7]
print("Test 3 - Sorted List:", sort(test3))

# Test case 4: List with negative numbers
test4 = [-1, -4, 3, 2, -6, 0]
print("Test 4 - Sorted List:", sort(test4))

# Test case 5: Already sorted list
test5 = [1, 2, 3, 4, 5]
print("Test 5 - Sorted List:", sort(test5))

# Test case 6: List sorted in reverse order
test6 = [5, 4, 3, 2, 1]
print("Test 6 - Sorted List:", sort(test6))

# Test case 7: Empty list
test7 = []
print("Test 7 - Sorted List:", sort(test7))
