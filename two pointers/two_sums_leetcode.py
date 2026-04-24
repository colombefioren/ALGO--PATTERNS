def two_sum(arr,target):
    left,right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current < target:
            left += 1

        elif current > target:
            right -= 1

        else:
            return [left + 1, right + 1]
        
    return []

print(two_sum([-1,0],-1))