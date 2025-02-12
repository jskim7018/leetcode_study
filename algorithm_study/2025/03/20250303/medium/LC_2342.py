from typing import List
from collections import Counter


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mp = dict()
        nums.sort(reverse=True)

        ans = -1
        for num in nums:
            num_digit_sum = 0
            tmp = num
            while tmp != 0:
                num_digit_sum += tmp % 10
                tmp //= 10
            if num_digit_sum in mp and mp[num_digit_sum] != -1:
                ans = max(ans, num + mp[num_digit_sum])
                mp[num_digit_sum] = -1
            else:
                mp[num_digit_sum] = num

        return ans
