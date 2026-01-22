from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # TODO: one-pass 방법도 있다.... one-pass 방법 확실히 익히기.
        n = len(nums)
        suffix_min = list(nums)

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i], suffix_min[i+1])

        curr_max = 0
        for i in range(n-1):
            curr_max = max(curr_max, nums[i])
            if curr_max <= suffix_min[i+1]:
                return i + 1

        return -1
