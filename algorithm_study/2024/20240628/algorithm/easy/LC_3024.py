from typing import List
from collections import Counter

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sum_ = sum(nums)
        max_ = max(nums)
        if max_ >= sum_ - max_:
            return "none"

        counter = Counter()
        for num in nums:
            counter[num] += 1

        if len(counter) == 1:
            return "equilateral"
        elif len(counter) == 2:
            return "isosceles"
        else:
            return "scalene"
