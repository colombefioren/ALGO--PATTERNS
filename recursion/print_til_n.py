class Solution:
    def printTillN(self, N):
        result = []

        def recursion(n):
            if n > N:
                return
            result.append(n)
            recursion(n + 1)

        recursion(1)

        print(" ".join(map(str, result)))

Solution().printTillN(1)