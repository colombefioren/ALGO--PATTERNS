class Solution:
    def combinationSum(self,candidates,target):
        result = []

        def backtrack(start,path):

            if sum(path) > target:
                return

            if sum(path) == target:
                result.append(path[:])
                return
        
            for i in range(start,len(candidates)):
                
                path.append(candidates[i])
                backtrack(i,path)
                path.pop()

        backtrack(0,[])
        return result


print(Solution().combinationSum([2,3,6,7],7))