def find_longest_chain(arr):
    arr_set = set(arr)
    longest_streak = []
    for num in arr_set:
        if num - 1 not in arr_set:
            current_num = num
            current_streak = [num]

            while current_num + 1 in arr_set:
                current_num += 1
                current_streak.append(current_num)

            if len(longest_streak)<len(current_streak):
                longest_streak = current_streak

    return longest_streak



print(find_longest_chain([1,2,3,4,1]))