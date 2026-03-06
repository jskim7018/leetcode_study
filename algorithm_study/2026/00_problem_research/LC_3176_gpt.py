from typing import List
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[j][val] = max length ending with val using j transitions
        dp = [defaultdict(int) for _ in range(k + 1)]
        best = [0] * (k + 1)

        for x in nums:
            # iterate backwards so we don't overwrite needed states
            for j in range(k, -1, -1):
                # extend same value
                same = dp[j][x] + 1

                # change value
                change = 0
                if j > 0:
                    change = best[j - 1] + 1

                dp[j][x] = max(dp[j][x], same, change)  # max(현재 것 안쓰는, 이전에 현재 것과 같은 것을 쓰는, 이전에 현재 것과 다른 것을 쓰는)
                best[j] = max(best[j], dp[j][x])

        return max(best)
