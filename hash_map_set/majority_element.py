def majority_element(nums):
    hash={}

    for num in (nums):
        hash[num]=hash.get(num,0)+1

    return list(sorted(hash.items(),key=lambda x: x[1],reverse=True))[0][0]


nums = [2,2,1,1,1,2,2]

majority_element(nums)