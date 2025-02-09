from typing import List
from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        counter = Counter()

        for i in range(n):
            counter[nums[i] - i] += 1

        good_pairs = 0
        for v in counter.values():
            good_pairs += (v*(v-1))//2

        bad_pairs = (n*(n-1))//2 - good_pairs

        return bad_pairs
