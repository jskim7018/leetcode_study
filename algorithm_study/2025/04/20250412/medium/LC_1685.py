from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = []

        sum_ = 0
        for i in range(1, n):
            sum_ += abs(nums[0] - nums[i])

        result.append(sum_)
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            sum_ += (i-1)*diff - (n-i-1)*diff
            result.append(sum_)

        return result
