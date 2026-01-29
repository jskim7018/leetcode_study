from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        curr_even = 0
        curr_odd = 0
        left_most_xor = dict()
        left_most_xor[(0,0)] = -1

        n = len(nums)
        curr_xor = 0
        ans = 0
        for i in range(n):
            curr_xor ^= nums[i]
            if nums[i] % 2 == 0:
                curr_even += 1
            else:
                curr_odd += 1
            key = (curr_xor, curr_even-curr_odd)
            if key in left_most_xor:
                left = left_most_xor[key] + 1
                ans = max(ans, i - left + 1)
            else:
                left_most_xor[key] = i

        return ans
