from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()

        ans = nums[-1] + nums[-2] - nums[0]

        return ans
