class Solution:
    def subset(self,nums):
        result = []
        def backtracking(index,path):
            
            if index == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[index])
            backtracking(index+1,path) 
            path.pop()

            backtracking(index+1,path)
        

        backtracking(0,[])
        return result



print(Solution().subset([1,2,2]))