from typing import List
from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                counter[nums[i]*nums[j]] += 1

        ans = 0

        for c in counter.values():
            ans += c*(c-1)*2*2
        return ans
