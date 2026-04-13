from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(start, n):
            if nums[i] == target:
                ans = min(ans, abs(i-start))
                break
        for i in range(start, -1, -1):
            if nums[i] == target:
                ans = min(ans, abs(i-start))
                break

        return ans
