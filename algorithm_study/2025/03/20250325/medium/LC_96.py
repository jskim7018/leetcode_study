from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:

        @cache
        def solve(n) -> int:
            if n == 1:
                return 1
            if n == 0:
                return 1

            ret = 0
            n -= 1
            for i in range(0, n + 1):
                ret += solve(i) * solve(n-i)
            return ret

        return solve(n)