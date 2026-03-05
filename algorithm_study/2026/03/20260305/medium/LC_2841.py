from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # Simple sliding window problem
        n = len(nums)

        counter = defaultdict(int)

        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
            counter[nums[i]] += 1

        ans = 0
        if len(counter) >= m:
            ans = curr_sum
        for i in range(k, n):
            curr_sum += -nums[i-k] + nums[i]

            counter[nums[i-k]] -= 1
            if counter[nums[i-k]] == 0:
                del counter[nums[i-k]]
            counter[nums[i]] += 1

            if len(counter) >= m:
                ans = max(ans, curr_sum)
        return ans
