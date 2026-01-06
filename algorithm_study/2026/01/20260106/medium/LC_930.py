from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        counter = defaultdict(int)

        accum = 0
        counter[accum] = 1
        for num in nums:
            accum += num
            ans += counter[accum-goal]
            counter[accum] += 1

        return ans
