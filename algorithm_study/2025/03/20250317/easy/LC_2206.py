from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for v in counter.values():
            if v % 2 == 1:
                return False

        return True
