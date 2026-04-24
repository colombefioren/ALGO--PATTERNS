def max_sum_subbarray(arr,k):
    window_sum = sum(arr[:k])
    start = 0
    end = k - 1
    max_sum = window_sum

    for i in range(k,len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        if(max_sum < window_sum):
            max_sum = window_sum
            start = i - k + 1
            end = i

    return arr[start:end + 1]

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subbarray(arr,k))