from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float('inf')

        for s, t in tasks:
            ans = min(ans, s+t)

        return ans
