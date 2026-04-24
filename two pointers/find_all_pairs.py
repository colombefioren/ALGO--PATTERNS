def find_all_pairs_sorted(arr, target=10):
    """
    Find ALL unique pairs in a SORTED array that sum to target.
    Returns list of pairs.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            pairs.append([arr[left], arr[right]])
            left += 1
            right -= 1
            
            # Skip duplicates if needed
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

# Example usage
arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(find_all_pairs_sorted(arr, 10))  # Output: [[1,9], [2,8], [3,7], [4,6], [5,5]]