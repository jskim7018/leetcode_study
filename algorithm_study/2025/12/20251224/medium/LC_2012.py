from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        max_from_left = list(nums)
        min_from_right = list(nums)

        for i in range(1, n):
            max_from_left[i] = max(nums[i], max_from_left[i-1])
            min_from_right[-i-1] = min(nums[-i-1], min_from_right[-i])

        ans = 0
        for i in range(1, n-1):
            if max_from_left[i-1] < nums[i] < min_from_right[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans
