class Solution:
    def subset(self,nums):
        result = []
        def backtracking(index,path):
            
            result.append(path[:])
            
            for i in range(index,len(nums)):

                path.append(nums[i])
                backtracking(i+1,path) 
                path.pop()


        backtracking(0,[])
        return result



print(Solution().subset([1,2]))