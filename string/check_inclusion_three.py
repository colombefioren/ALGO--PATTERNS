def check_inclusion(s1,s2):
    n,m=len(s1),len(s2)
    if m < n:
        return False

    target = [0] * 26
    window = [0] * 26

    for s in s1:
        target[ord(s)-ord("a")] += 1

    for s in s2[:n]:
        window[ord(s)-ord("a")] += 1

    if window == target:
        return True
    
    for i in range(n,m):
        window[ord(s2[i])-ord("a")] += 1
        window[ord(s2[i-n])-ord("a")] -= 1

        if window == target:
            return True

    return False

print(check_inclusion("ab","eidbaooo"))
