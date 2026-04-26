def is_palindrome(s):
    """
    Check if a string is palindrome using recursion.
    
    Time: O(n), Space: O(n) due to recursion stack
    """
    # Base case: empty string or single character is palindrome
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check substring without first and last chars
    return is_palindrome(s[1:-1])