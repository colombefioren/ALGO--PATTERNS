def is_palindrome(s):
    alpha = "".join([l.lower() for l in s if l.isalnum()])

    right=len(alpha)-1
    left=0
    while(left<right):
        if alpha[left] != alpha[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("a"))