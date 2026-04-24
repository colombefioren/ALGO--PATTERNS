def group_anagrams(strs):
    """
    Group anagrams together.
    
    Time: O(n * k log k) where k is max string length
    Space: O(n * k)
    """
    
    anagram_groups = {}

    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))