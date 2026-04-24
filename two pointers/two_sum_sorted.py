def two_sum_sorted(arr, target=10):
    """
    Find two numbers in a SORTED array that sum to target.
    Returns indices or values.
    Time: O(n), Space: O(1)
    """
    left,right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [arr[left],arr[right]]
        
        elif current < target:
            left += 1

        else:
            right -= 1

    return []

arr = [1, 2, 3, 4, 5, 6, 8]
print(two_sum_sorted(arr, 7))  # Output: [3, 5] (4 + 6 = 10)