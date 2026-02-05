from typing import List
import heapq


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        min_heap = []

        prev_row_xor = [0] * n
        for i in range(m):
            curr_row_xor = [0] * n
            xored = 0
            for j in range(n):
                xored ^= matrix[i][j]
                curr_row_xor[j] ^= xored ^ prev_row_xor[j]
                heapq.heappush(min_heap, curr_row_xor[j])
                while len(min_heap) > k:
                    heapq.heappop(min_heap)
            prev_row_xor = curr_row_xor
        return min_heap[0]
