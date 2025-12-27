from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        ans = []
        for i in range(n):
            if i > 0 and nums[i] - nums[i-1] <= 1:
                continue
            if i+1 < n and nums[i+1] - nums[i] <= 1:
                continue
            ans.append(nums[i])

        return ans
