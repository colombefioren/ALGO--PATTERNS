def check_inclusion(s1,s2):
    if len(s2) < len(s1):
        return False

    left = 0
    right = left + 1

    while right <= len(s2):
        if s2[left] in list(s1):
            while right - left < len(s1):
                right += 1
        if "".join(sorted(s1)) == "".join(sorted(s2[left:right])):
            return True
        right += 1
        left += 1
    return False

print(check_inclusion("ab","eidbaooo"))
