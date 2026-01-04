from functools import lru_cache
import math


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0

        n = math.ceil(n)

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5 # 같이 떨어질 확률의 반을 구하는 것 이기에 0.5로 한것. 따로 구할 필요 없이 한번에 구함.
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25* (
                    dp(a - 100, b) +
                    dp(a - 75, b - 25) +
                    dp(a - 50, b - 50) +
                    dp(a - 25, b - 75)
            )

        return dp(n, n)