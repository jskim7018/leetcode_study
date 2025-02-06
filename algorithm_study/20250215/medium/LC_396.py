from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sum = sum(nums)

        curr_func_sum = 0
        for i in range(n):
            curr_func_sum += nums[i] * i

        ans = curr_func_sum
        for i in range(n):
            curr_func_sum -= nums_sum
            curr_func_sum += nums[i] * (n)
            ans = max(ans, curr_func_sum)

        return ans
