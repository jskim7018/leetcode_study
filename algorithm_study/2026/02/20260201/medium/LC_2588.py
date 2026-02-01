from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix_xor_freq = defaultdict(int)

        ans = 0
        curr_prefix_xor = 0
        prefix_xor_freq[0] = 1
        for num in nums:
            curr_prefix_xor ^= num
            ans += prefix_xor_freq[curr_prefix_xor]
            prefix_xor_freq[curr_prefix_xor] += 1

        return ans
