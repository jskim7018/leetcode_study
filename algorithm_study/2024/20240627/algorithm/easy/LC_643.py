from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum_ = sum([num for num in nums[:k]])
        ans = sum_/k
        for i in range(k, len(nums)):
            sum_ = sum_ - nums[i-k] + nums[i]
            ans = max(ans, sum_/k)
        return ans
