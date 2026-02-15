from typing import List
from collections import Counter


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        # 1. Get frequencies, then get frequencies of frequencies
        # 2. Then sweep

        counter = Counter(nums)
        counter_of_counter = Counter(counter.values())

        for num in nums:
            if counter_of_counter[counter[num]] == 1:
                return num
        return -1
