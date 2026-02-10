from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # values[i] + values[j] + i - j => (values[i]+i) + (values[j]-j)
        # use heap and do lazy deletion.
        # or without heap just use max suffix. 2 pass
        # or go iterate from back and do it in 1 pass with O(1) memory
        n = len(values)
        max_suffix = values[-1] - (n-1)
        ans = 0
        for i in range(n-2, -1, -1):
            ans = max(ans, values[i] + i + max_suffix)
            max_suffix = max(max_suffix, values[i]-i)

        return ans
