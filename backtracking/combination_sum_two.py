class Solution:
    def combinationSum2(self,candidates,target):
        result = []
        candidates.sort()
        def backtrack(start,path):

            if sum(path) > target:
                return

            if sum(path) == target:
                result.append(path[:])
                return
        
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return result


print(Solution().combinationSum2([10,1,2,7,6,1,5],8))