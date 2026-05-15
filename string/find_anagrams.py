def find_anagrams(s,p):
    n,m = len(p),len(s)

    result = []

    if n > m:
        return result
    
    target = [0] * 26
    window = [0] * 26

    for ch in p:
        target[ord(ch) - ord("a")] += 1
    
    for ch in s[:n]:
        window[ord(ch) - ord("a")] += 1
    
    if window == target:
        result.append(0)

    for i in range(n,m):
        window[ord(s[i])-ord("a")] += 1
        window[ord(s[i-n]) - ord("a")] -= 1

        if window == target:
            result.append(i-n+1)

    return result

print(find_anagrams("cbaebabacd","abc"))