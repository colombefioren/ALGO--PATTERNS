def is_valid_anagram(wone,wtwo):
    if len(wone) != len(wtwo):
        return False
    
    letter_count = {}

    for l in wone:
        letter_count[l] = letter_count.get(l,0) + 1

    for l in wtwo:
        if l not in letter_count:
            return False
        letter_count[l] -= 1
        if letter_count[l] == 0:
            del letter_count[l]

    return len(letter_count) == 0


print(is_valid_anagram('admiretr','marrietd'))
    