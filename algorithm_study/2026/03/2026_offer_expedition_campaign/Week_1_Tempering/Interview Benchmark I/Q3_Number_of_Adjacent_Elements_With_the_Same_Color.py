from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n

        same_color_adj_cnt = 0
        ans = []
        for q in queries:
            idx, color = q

            if colors[idx] != 0:
                if idx - 1 >= 0 and colors[idx-1] == colors[idx]:
                    same_color_adj_cnt -= 1
                if idx + 1 < n and colors[idx] == colors[idx+1]:
                    same_color_adj_cnt -= 1

            colors[idx] = color
            if idx - 1 >= 0 and colors[idx - 1] == colors[idx]:
                same_color_adj_cnt += 1
            if idx + 1 < n and colors[idx] == colors[idx + 1]:
                same_color_adj_cnt += 1

            ans.append(same_color_adj_cnt)

        return ans
