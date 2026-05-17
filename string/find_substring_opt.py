def find_substring(s: str, words: list[str]):
        ans = []

        if not words or not s:
            return ans

        word_size = len(words[0])
        word_count = len(words)
        N = len(s)

        original_count = {}

        for word in words:
            original_count[word] = original_count.get(word, 0) + 1

        for offset in range(word_size):

            current_count = {}
            start = offset
            count = 0

            for end in range(offset, N - word_size + 1, word_size):

                curr_word = s[end:end + word_size]

                if curr_word in original_count:

                    current_count[curr_word] = (
                        current_count.get(curr_word, 0) + 1
                    )

                    count += 1

                    while (
                        current_count[curr_word]
                        > original_count[curr_word]
                    ):

                        start_word = s[start:start + word_size]

                        current_count[start_word] -= 1

                        start += word_size
                        count -= 1

                    if count == word_count:
                        ans.append(start)

                else:
                    count = 0
                    start = end + word_size
                    current_count.clear()

        return ans

print(find_substring("barfoothefoobarman", ["foo", "bar"]))