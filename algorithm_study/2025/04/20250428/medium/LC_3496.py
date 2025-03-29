from typing import List

# TODO: Study optimal solution
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0

        left_sums = [float('-inf')] * n
        right_sums = [float('-inf')] * n

        curr_sum_l = 0
        curr_sum_r = 0
        for i, num in enumerate(nums):
            curr_sum_l += num
            curr_sum_r += nums[n-i-1]
            left_sums[i] = curr_sum_l
            right_sums[n-i-1] = curr_sum_r

        ans = float('-inf')
        for i in range(n):
            curr = 0
            if n % 2 == 0:
                even_curr1 = 0
                even_curr2 = 0
                if i-2 >=0:
                    even_curr1 += left_sums[i - 2]
                if i + 1 < n and i != 0:
                    even_curr1 += right_sums[i + 1]

                if i - 1 >= 0 and i != n-1:
                    even_curr2 += left_sums[i-1]
                if i + 2 < n:
                    even_curr2 += right_sums[i+2]
                if i == 0:
                    even_curr1 = float('-inf')
                if n-1:
                    even_curr2 = float('-inf')
                curr = max(even_curr1, even_curr2)
            else:
                if i - 1 >= 0:
                    curr += left_sums[i-1]
                if i + 1 < n:
                    curr += right_sums[i+1]

            ans = max(ans, curr)

        return ans
