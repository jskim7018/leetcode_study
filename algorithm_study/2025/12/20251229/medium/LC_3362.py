from typing import List
import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort()
        r_max_heap = []

        q_idx = 0
        line_sweep = [0] * n
        for i in range(n):
            while q_idx < len(queries):
                if queries[q_idx][0] <= i:
                    heapq.heappush(r_max_heap, -queries[q_idx][1])
                    q_idx += 1
                else:
                    break
            if i > 0:
                line_sweep[i] += line_sweep[i-1]
            need = max(0, nums[i] - line_sweep[i])
            while need:
                if not r_max_heap:
                    return -1
                nxt = -heapq.heappop(r_max_heap)
                if nxt < i:
                    return - 1
                line_sweep[i] += 1
                if nxt + 1 < n:
                    line_sweep[nxt+1] -= 1
                need -= 1

        return len(r_max_heap)
