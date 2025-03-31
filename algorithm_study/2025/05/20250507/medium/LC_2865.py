from typing import List


# TODO: Do it more efficiently
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)

        ans = 0
        for mid in range(n):
            l = mid-1
            r = mid+1

            bef = heights[mid]
            sum_ = bef
            for i in range(l, -1,-1):
                if heights[i] > bef:
                    bef = bef
                else:
                    bef = heights[i]
                sum_ += bef

            bef = heights[mid]
            for i in range(r, n):
                if heights[i] > bef:
                    bef = bef
                else:
                    bef = heights[i]
                sum_ += bef
            ans = max(ans, sum_)

        return ans
