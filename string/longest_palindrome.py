def longest_palindrome(s):
    l=0
    r=l+1
    max_str=""
    f=False
    while r<len(s):
        if s[l]==s[r]:
            if len(max_str)<r-l+1:
                max_str=s[l:r+1]
                f=True
            r+=1
        if s[l]!=s[r]:
            if f:
                l += 1
            else:
                r += 1
            f=False
    return max_str

print(longest_palindrome("mlml"))

