from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7

        _min = min(complexity)
        cnt_min = complexity.count(_min)

        if _min != complexity[0] or cnt_min != 1:
            return 0
        else:
            rearrange_n = len(complexity) - 1
            ans = 1
            for i in range(1,rearrange_n+1):
                ans *= i
                ans %= mod

            return ans
