def find_max_consecutive_ones(nums):
    current=0
    max_count=current
    for i in range(len(nums)):
        if nums[i] != 0:
            current += 1
        else:
            current=0
        max_count=max(max_count,current)
    return max_count

print(find_max_consecutive_ones([1,0,1,1,0,1]))