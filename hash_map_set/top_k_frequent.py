def top_k_frequent(nums,k):
    hash={}

    for num in (nums):
        hash[num]=hash.get(num,0)+1

    return [x[0] for x in sorted(hash.items(),key=lambda x: x[1],reverse=True)[:k]]


print(top_k_frequent([1,1,1,2,2,3],2))
