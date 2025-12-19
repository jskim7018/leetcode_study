from typing import List
from collections import Counter


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        print(counter)
        ans = 0

        for v, f in counter.items():
            if f % k == 0:
                ans += f * v

        return ans
