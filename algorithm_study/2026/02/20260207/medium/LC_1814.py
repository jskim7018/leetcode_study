from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # find number of pairs that are reverse that does not end with 0.
        # and finding number of pairs that are palindromes.
        # except 0 itself.
        mod = 10**9 + 7

        num_rev_diff_count = defaultdict(int)

        ans = 0
        for num in nums:
            num_rev = int(str(num)[::-1])
            ans += num_rev_diff_count[num_rev - num]
            ans %= mod
            num_rev_diff_count[num_rev - num] += 1

        return ans
