def find_substring(s: str, words: list[str]):
    m = len(s)
    n = len(words[0])

    need = {}
    for w in words:
        need[w] = need.get(w, 0) + 1

    result = []

    total_len = n * len(words)

    for left in range(m - total_len + 1):
        window = s[left:left + total_len]

        seen = {}
        valid = True

        for i in range(0, total_len, n):
            word = window[i:i + n]

            if word not in need:
                valid = False
                break

            seen[word] = seen.get(word, 0) + 1

            if seen[word] > need[word]:
                valid = False
                break

        if valid:
            result.append(left)

    return result


print(find_substring("barfoothefoobarman", ["foo", "bar"]))