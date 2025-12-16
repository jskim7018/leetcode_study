from typing import List
import heapq


class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        n = len(nums)

        items = [(t, n) for t, n in zip(threshold, nums)]
        items.sort()

        heap = []
        heapq.heapify(heap)

        step = 1
        ans = 0
        curr_item_idx = 0
        while True:
            while curr_item_idx < n and items[curr_item_idx][0] <= step:
                heapq.heappush(heap, -items[curr_item_idx][1])
                curr_item_idx += 1
            if not heap:
                break
            ans += -heapq.heappop(heap)

            step += 1

        return ans
