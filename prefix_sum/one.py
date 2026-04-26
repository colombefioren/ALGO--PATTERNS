class PrefixSum:
    """
    Prefix sum allows O(1) queries for sum of any subarray after O(n) preprocessing.
    
    prefix_sum[i] = sum of elements from index 0 to i-1
    sum(arr[left...right]) = prefix_sum[right+1] - prefix_sum[left]
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        # Build prefix sum array (size n+1, prefix[0] = 0)
        self.prefix = [0] * (self.n + 1)
        for i in range(self.n):
            self.prefix[i + 1] = self.prefix[i] + arr[i]
    
    def sum_range(self, left, right):
        """
        Calculate sum of subarray from index left to right (inclusive).
        Time: O(1)
        """
        if left < 0 or right >= self.n or left > right:
            return 0
        return self.prefix[right + 1] - self.prefix[left]
    
    def sum_all_queries(self, queries):
        """
        Process multiple subarray sum queries.
        
        Args:
            queries: List of tuples [(left1, right1), (left2, right2), ...]
        Returns:
            List of sums for each query
        """
        return [self.sum_range(left, right) for left, right in queries]

# Example usage
arr = [2, 3, 5, 1, 4, 7]
ps = PrefixSum(arr)
print(ps.prefix)  # [0, 2, 5, 10, 11, 15, 22]

# Calculate sum of subarray [2, 5, 1] (indices 1 to 3)
print(ps.sum_range(1, 3))  # Output: 9 (3 + 5 + 1)

# Multiple queries
queries = [(0, 2), (1, 4), (2, 5), (0, 5)]
print(ps.sum_all_queries(queries))  # Output: [10, 13, 17, 22]