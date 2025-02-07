from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            set_ = set()
            for j in range(i, len(nums)):
                set_.add(nums[j])
                ans += len(set_) ** 2
        return ans
