from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)

        _sum = sum(beans)

        beans.sort()

        ans = float('inf')
        curr_sum = 0
        for i, b in enumerate(beans):
            rest = _sum - curr_sum - b
            ans = min(ans, curr_sum + rest - (b * (n-i-1)))
            curr_sum += b

        return ans
