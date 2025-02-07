from typing import List
from collections import Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        all_st = set(nums)

        n = len(nums)

        l = 0

        ans = 0
        for i in range(n):
            counter = Counter()
            for j in range(i, n):
                counter[nums[j]] += 1
                if len(counter) == len(all_st):
                    ans += 1

        return ans
