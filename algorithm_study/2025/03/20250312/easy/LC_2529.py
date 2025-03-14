from typing import List


# TODO: Solve with binary tree
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt_neg = 0
        cnt_pos = 0
        for num in nums:
            if num > 0:
                cnt_pos += 1
            elif num < 0:
                cnt_neg += 1

        return max(cnt_pos, cnt_neg)
