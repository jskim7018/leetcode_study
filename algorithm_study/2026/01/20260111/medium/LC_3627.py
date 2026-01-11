from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        n = len(nums)

        cnt_get = n//3
        ans = 0
        for i in range(1, n, 2):
            if cnt_get == 0:
                break
            cnt_get -= 1
            ans += nums[i]

        return ans
