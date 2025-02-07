from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            minim = min(nums)

            for i, v in enumerate(nums):
                if v == minim:
                    nums[i] = v * multiplier
                    break

        return nums
