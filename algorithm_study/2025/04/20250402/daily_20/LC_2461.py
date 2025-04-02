from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0

        counter = defaultdict(int)

        sum_ = 0
        for i in range(k):
            counter[nums[i]] += 1
            sum_ += nums[i]
        if len(counter) == k:
            ans = max(ans, sum_)

        for i in range(1,n-k+1):
            sum_ = sum_ - nums[i-1] + nums[i+k-1]
            counter[nums[i-1]] -= 1
            if counter[nums[i-1]] == 0:
                del counter[nums[i-1]]
            counter[nums[i+k-1]] += 1

            if len(counter) == k:
                ans = max(ans, sum_)

        return ans
