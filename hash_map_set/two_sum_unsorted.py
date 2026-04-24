def two_sum_unsorted(arr,target):
    """
    Find two numbers in an unsorted array that sum to target
    returns index
    Time: O(n), Space: O(n)
    """

    seen = {}

    for i,num in enumerate(arr):
        complement = target - num
        
        if complement in seen:
            return [seen[complement],i]
        
        seen[num] = i

    
    return []



arr = [3, 5, 2, 8, 1, 4]
print(two_sum_unsorted(arr, 10)) 