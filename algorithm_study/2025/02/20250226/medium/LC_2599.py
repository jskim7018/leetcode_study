from typing import List
import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n

        neg_heap = []
        heapq.heapify(neg_heap)

        ans = 0
        for i in range(n):
            prefix_sum[i] += nums[i]
            if nums[i] < 0:
                heapq.heappush(neg_heap, nums[i])
            if i > 0:
                prefix_sum[i] += prefix_sum[i-1]
            if prefix_sum[i] < 0:
                ans += 1
                prefix_sum[i] -= heapq.heappop(neg_heap)

        return ans