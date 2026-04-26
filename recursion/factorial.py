def factorial(n):
    """
    Calculate factorial using recursion.
    
    factorial(n) = n * (n-1) * (n-2) * ... * 1
    
    Time: O(n), Space: O(n)
    """
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)