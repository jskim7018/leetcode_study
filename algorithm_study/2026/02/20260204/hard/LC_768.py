from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        sorted_arr = [(num, i) for i, num in enumerate(arr)]
        sorted_arr.sort()
        sorted_idx = dict()
        for i in range(n):
            sorted_idx[sorted_arr[i][1]] = i

        chunk_cnt = 0
        curr_max_idx = 0
        for i in range(n):
            s_idx = sorted_idx[i]
            curr_max_idx = max(curr_max_idx, s_idx)
            if curr_max_idx == i:
                chunk_cnt += 1

        return chunk_cnt
