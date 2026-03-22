from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        arr = list(counter.items())

        arr.sort(key=lambda x: -x[1])

        return [val for val, _ in arr[:k]]
