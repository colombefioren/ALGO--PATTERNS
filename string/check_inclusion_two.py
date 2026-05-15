def check_inclusion(s1, s2):
    n, m = len(s1), len(s2)
    if n > m:
        return False

    target = {}

    for s in s1:
        target[s] = target.get(s,0) + 1

    window = {}

    for s in s2[:n]:
        window[s] = window.get(s,0) + 1
    
    if window == target:
        return True

    for i in range(n,m):
        window[s2[i]] = window.get(s2[i],0) + 1
        window[s2[i - n]] -= 1

        if window[s2[i - n]] == 0:
            del window[s2[i-n]]
        
        if window == target:
            return True

    return False



print(check_inclusion("ab", "eidbaooo"))