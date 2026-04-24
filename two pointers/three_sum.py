def three_sum(nums):
    nums.sort()
    triplet = []

    for i in range(len(nums)):
       

        if i > 0 and nums[i] == nums[i -1]:
            continue

        if nums[i] > 0:
            break
        
        j,k = i + 1,len(nums) - 1

        while j < k:
            current = nums[i] + nums[j] + nums[k]
            if current == 0:
                triplet.append([nums[i],nums[j],nums[k]])
                j+= 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j+=1
                while j < k and nums[k] == nums[k+1]:
                    k-=1
            
            elif current < 0:
                j += 1                                          

            else:
                k -= 1
        
    return triplet                                              


print(three_sum([-2,0,1,1,2]))

