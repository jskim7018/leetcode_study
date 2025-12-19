from typing import List
from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        counter = Counter()

        for i in range(0, n-k+1):
            visited = set()
            for j in range(k):
                if nums[i+j] not in visited:
                    counter[nums[i+j]] += 1
                    visited.add(nums[i+j])

        ans = -1
        for e, v in counter.items():
            if v == 1:
                ans = max(ans, e)

        return ans
