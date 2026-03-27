from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        # If possible it is always better to do div 2 or div 3
        # so make it possible that we can do div 2 or div 3 then do it.
        # If only 1 or 0 is left then just return that since cant div by 2 or 3.
        @lru_cache(None)
        def dfs(n):
            if n <= 1:
                return n

            # option 1: make divisible by 2
            div2 = n % 2 + dfs(n // 2)

            # option 2: make divisible by 3
            div3 = n % 3 + dfs(n // 3)

            return 1 + min(div2, div3)

        return dfs(n)
