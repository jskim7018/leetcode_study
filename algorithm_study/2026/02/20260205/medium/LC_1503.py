from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        if left:
            ans = max(left)
        if right:
            ans = max(ans, n - min(right))

        return ans
