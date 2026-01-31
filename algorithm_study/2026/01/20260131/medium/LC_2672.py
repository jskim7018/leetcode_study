from typing import List
from collections import defaultdict


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        idx_to_color = [0] * n

        ans = []
        curr_adj_pairs = 0
        for q in queries:
            idx, color = q

            if idx_to_color[idx] != 0:
                if idx-1 >= 0 and idx_to_color[idx-1] == idx_to_color[idx]:
                    curr_adj_pairs -= 1
                if idx + 1 < n and idx_to_color[idx + 1] == idx_to_color[idx]:
                    curr_adj_pairs -= 1

            idx_to_color[idx] = color
            if idx-1 >= 0 and idx_to_color[idx - 1] == idx_to_color[idx]:
                curr_adj_pairs += 1
            if idx + 1 < n and idx_to_color[idx + 1] == idx_to_color[idx]:
                curr_adj_pairs += 1
            ans.append(curr_adj_pairs)

        return ans
