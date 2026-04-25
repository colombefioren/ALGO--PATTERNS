def max_sum_subbarray(arr,k):
    window_sum = 0
    max_sum=window_sum

    for right in range(len(arr)):
        for i in range(k):
            print(i)
            if arr[i] == arr[i-1]:
                print(arr[i],arr[i-1])
                break
            window_sum += arr[i]
        max_sum=max(max_sum,window_sum)
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subbarray(arr,k))