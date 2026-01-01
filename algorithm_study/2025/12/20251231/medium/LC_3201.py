from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_cnt = 0
        odd_cnt = 0
        alt_cnt = 1
        curr_alt = nums[0] % 2
        for num in nums:
            if num % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

            if num % 2 != curr_alt:
                curr_alt = num % 2
                alt_cnt += 1

        return max(even_cnt, odd_cnt, alt_cnt)
