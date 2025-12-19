from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        ans = []
        for i in range(1, n):
            for num in range(nums[i - 1] + 1, nums[i]):
                ans.append(num)

        return ans
