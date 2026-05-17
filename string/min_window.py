def min_window(s:str,t:str):
    m,n=len(s),len(t)

    need = {}
    for ch in t:
        need[ch] = need.get(ch,0)+1

    missing = n
    
    left = 0
    right = 0
    min_len = float("inf")

    for right in range(m):
        if s[right] in need:
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1

        while missing == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            if s[left] in need:
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
            left += 1
            
    return "" if min_len == float("inf") else s[start:start+min_len]

print(min_window("ADOBECODEBANC","ABC"))

