from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0

        ans = 0
        for t in target:
            if t > prev:
                ans += t-prev
            prev = t

        return ans
