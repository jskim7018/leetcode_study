from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0

        i = 0
        while i < n:
            start = i

            # find local min
            while i < n - 1 and nums[i] > nums[i + 1]:
                i += 1

            # score every second number backwards
            j = i
            while j >= start:
                score += nums[j]
                j -= 2

            i += 2

        return score
