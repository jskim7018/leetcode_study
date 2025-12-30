from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        subsequence_cnt = 1

        curr_minim = nums[0]
        for i in range(1, n):
            if nums[i] - curr_minim > k:
                curr_minim = nums[i]
                subsequence_cnt += 1

        return subsequence_cnt
