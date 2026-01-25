from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        keep = 1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                keep += 1
            else:
                break

        return n - keep
