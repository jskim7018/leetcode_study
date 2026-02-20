from functools import lru_cache


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:

        @lru_cache(None)
        def dfs(x):
            if x <= y:
                return y - x

            # Direct decrement
            ans = x - y

            # Try divide by 5
            r = x % 5
            if r == 0:
                ans = min(ans, 1 + dfs(x // 5))
            else:
                # decrement to multiple
                ans = min(ans, r + 1 + dfs(x // 5))
                # increment to next multiple
                ans = min(ans, (5 - r) + 1 + dfs((x + (5 - r)) // 5))

            # Try divide by 11
            r = x % 11
            if r == 0:
                ans = min(ans, 1 + dfs(x // 11))
            else:
                ans = min(ans, r + 1 + dfs(x // 11))
                ans = min(ans, (11 - r) + 1 + dfs((x + (11 - r)) // 11))

            return ans

        return dfs(x)
