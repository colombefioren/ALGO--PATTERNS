def longest_palindrome(s:str)->str:
    start = 0
    end = 0
    for i in range(len(s)):
        len_odd = expand(s,i,i)
        len_even = expand(s,i,i+1)

        current_len = max(len_even,len_odd)

        if current_len > end - start:
            start = i - (current_len - 1) //2 
            end = i + (current_len // 2)

    return s[start:end+1]

def expand(s:str,left:int,right:int)->int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

print(longest_palindrome("babad"))


