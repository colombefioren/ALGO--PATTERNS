def min_window(s:str,t:str):
    m=len(s)
    target={}
    for ch in t:
        target[ch] = target.get(ch,0) + 1
    sum = target.copy()
    min_len=float("inf")
    result = ""
    right = 0
    for left in range(m):
        right = left
        while len(sum) > 0 and right < m:
            if s[right] in sum:
                sum[s[right]] -= 1
                if sum[s[right]] == 0:
                    del sum[s[right]]
            right += 1
        
        if min_len > right - left +1 and len(sum) <= 0:
            min_len = right - left + 1
            result = s[left:right]

        sum = target.copy()
    return result

print(min_window("ADOBECODEBANC","ABC"))

