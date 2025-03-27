from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                nums.append(grid[i][j])

        nums.sort()
        n = len(nums)
        mid_val = nums[n//2]
        ans = 0
        for i in range(0,n):
            if i >= 1 and nums[i] % x != nums[i-1] % x:
                return -1
            ans += abs(mid_val - nums[i]) // x

        return ans
