def count_substrings(s:str)->int:
    count = 0
    for i in range(len(s)):
        count += expand(s,i,i)
        count += expand(s,i,i+1)
    return count


def expand(s:str,left:int,right:int)->int:
    count = 0
    while right < len(s) and left >= 0 and s[right] == s[left]:
        count += 1
        right += 1
        left -= 1
    return count

print(count_substrings("aaa"))