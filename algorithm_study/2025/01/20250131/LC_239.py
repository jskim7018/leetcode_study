import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heap.append((-nums[i], i))

        heapq.heapify(heap)

        ans = []
        ans.append(heapq.nsmallest(1, heap)[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] < i-k+1:
                heapq.heappop(heap)
            ans.append(heap[0][0])

        ans = [-x for x in ans]

        return ans
