from typing import List
from sortedcontainers import SortedSet
import heapq


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        heap = []
        sorted_set = SortedSet()
        for i in range(n):
            if nums[i] >= left and nums[i] <= right:
                heap.append((-nums[i], i))
            elif nums[i] > right:
                sorted_set.add(i)

        heapq.heapify(heap)
        ans = 0
        while heap:
            element = heapq.heappop(heap)
            idx = element[1]

            r_idx = sorted_set.bisect_left(idx)
            l_idx = r_idx-1

            l = -1
            r = n
            if r_idx < len(sorted_set):
                r = sorted_set[r_idx]
            if l_idx >= 0:
                l = sorted_set[l_idx]

            ans += (idx - l) * (r-idx)
            sorted_set.add(idx)

        return ans
