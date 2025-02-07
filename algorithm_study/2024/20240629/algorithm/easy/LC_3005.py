from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_ = 0
        counter = Counter()
        for num in nums:
            counter[num] += 1
            max_ = max(max_, counter[num])

        total_freq = 0
        for cnt in counter.values():
            if cnt == max_:
                total_freq += cnt

        return total_freq
