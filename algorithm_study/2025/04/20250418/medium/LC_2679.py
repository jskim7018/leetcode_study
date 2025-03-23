from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])

        for i in range(m):
            nums[i].sort()

        ans = 0
        for j in range(n):
            maxim = float('-inf')
            for i in range(m):
                maxim = max(maxim, nums[i][j])
            ans += maxim

        return ans
