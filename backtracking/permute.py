class Solution:
    def permute(self,nums):
        result = []
        def backtrack(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                path.append(nums[i])
                backtrack(path)
                path.pop()

        backtrack([])
        return result

print(Solution().permute([1,2,3]))