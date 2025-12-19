from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0

        for i in range(n):
            if (i-k < 0 or nums[i-k] < nums[i]) \
                and (i+k >= n or nums[i+k] < nums[i]):
                ans += nums[i]
        return ans
