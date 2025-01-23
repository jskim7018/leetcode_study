from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        suffix_sum = []

        # Construct suffix array
        for idx, num in enumerate(reversed(nums)):
            idx2 = len(nums)-idx-1
            sum = nums[idx2]
            if idx-1 >= 0:
                sum += suffix_sum[idx-1]
            suffix_sum.append(sum)

        suffix_sum.reverse()

        # Solve using suffix array
        total = 0
        for i in range(len(nums)):
            start = max(0, i-nums[i])
            total += suffix_sum[start]
            if i+1 < len(nums):
                total -= suffix_sum[i+1]

        return total
