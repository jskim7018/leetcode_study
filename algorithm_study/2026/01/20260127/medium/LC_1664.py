from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)

        total_even_sum = 0
        total_odd_sum = 0
        for i in range(n):
            if i % 2 == 0:
                total_even_sum += nums[i]
            else:
                total_odd_sum += nums[i]

        curr_even_sum = 0
        curr_odd_sum = 0
        ans = 0
        for i in range(n):
            ex_total_even_sum = curr_even_sum
            ex_total_odd_sum = curr_odd_sum

            if i % 2 == 0:
                curr_even_sum += nums[i]
            else:
                curr_odd_sum += nums[i]
                
            ex_total_even_sum += total_odd_sum - curr_odd_sum
            ex_total_odd_sum += total_even_sum - curr_even_sum

            if ex_total_even_sum == ex_total_odd_sum:
                ans += 1

        return ans