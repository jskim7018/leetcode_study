from typing import List
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        ans = right
        while left <= right:
            mid = (left+right)//2

            n_tmp = n
            for q in quantities:
                n_tmp -= math.ceil(q/mid)
            if n_tmp >= 0:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans
