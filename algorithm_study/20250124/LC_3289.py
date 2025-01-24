from typing import List
from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        return list(dict(counter.most_common(2)).keys())
