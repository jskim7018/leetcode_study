from typing import List
from collections import Counter


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        counter = Counter(nums)

        num_to_freq = [(e, v) for e, v in counter.items()]

        num_to_freq.sort()

        curr_freq_sum = 0

        ans = 0
        for i in range(len(num_to_freq)-1, -1, -1):
            freq = num_to_freq[i][1]
            if curr_freq_sum >= k:
                ans += freq
            curr_freq_sum += freq

        return ans
