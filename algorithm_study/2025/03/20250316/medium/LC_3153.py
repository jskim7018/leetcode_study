from typing import List
from collections import Counter


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        digit_len = len(str(nums[0]))

        ans = 0
        for i in range(digit_len):
            counter = Counter()
            for j in range(n):
                counter[nums[j] % 10] += 1
                nums[j] //= 10

            curr_n = n
            for k, v in counter.items():
                curr_n -= v
                ans += curr_n * v

        return ans
