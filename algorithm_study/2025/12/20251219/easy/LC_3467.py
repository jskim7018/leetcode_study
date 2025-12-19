from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_cnt = sum(1 for num in nums if num % 2 == 0)

        ans = [1] * len(nums)

        for i in range(even_cnt):
            ans[i] = 0

        return ans
