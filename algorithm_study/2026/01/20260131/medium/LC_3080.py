from typing import List
import heapq


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]

        total_sum = sum(nums)
        heapq.heapify(heap)

        deleted_idx = set()

        ans = []
        for q in queries:
            idx, k = q
            if idx not in deleted_idx:
                deleted_idx.add(idx)
                total_sum -= nums[idx]

            while heap and k:
                element, i = heapq.heappop(heap)
                if i in deleted_idx:
                    continue
                else:
                    deleted_idx.add(i)
                    total_sum -= element
                    k -= 1
            ans.append(total_sum)

        return ans
