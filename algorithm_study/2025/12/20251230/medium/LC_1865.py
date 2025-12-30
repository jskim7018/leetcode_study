from typing import List
from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter1 = Counter(nums1)
        self.counter2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        added_val = self.nums2[index] + val
        self.counter2[self.nums2[index]] -= 1
        self.counter2[added_val] += 1
        self.nums2[index] = added_val

    def count(self, tot: int) -> int:
        ans = 0
        for k, v in self.counter1.items():
            to_find = tot - k
            ans += self.counter2[to_find] * v

        return ans
