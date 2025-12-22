from typing import List
import heapq


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)

        heap = []

        ans = 0
        for i in range(n):
            heapq.heappush(heap, -nums[i])
            if s[i] == '1':
                ans += -heapq.heappop(heap)

        return ans
