from typing import List
from functools import cache


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        powers = []

        i = 0
        while n > 0:
            if n % 2 == 1:
                powers.append(2**i)
            n //= 2
            i += 1

        @cache
        def dp(l: int, r: int) -> int:
            if l == r:
                return powers[l]
            ret = powers[l]
            ret *= dp(l+1, r)
            ret %= mod
            return ret

        ans = []
        for q in queries:
            left = q[0]
            right = q[1]
            product = dp(left, right)
            ans.append(product)

        return ans
