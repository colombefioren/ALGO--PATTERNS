def longest_k_substr(s,k):
    n = len(s)
    seen = {}
    left = 0
    max_len = -1
    for right in range(n):
        seen[s[right]] = seen.get(s[right],0) + 1

        while len(seen) > k:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1

        if len(seen) == k:
            max_len = max(max_len, right - left + 1)
    
    return max_len

print(longest_k_substr('aabaaab',2))