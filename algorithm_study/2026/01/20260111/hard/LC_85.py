from typing import List
from collections import defaultdict


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        cont_one_cnt_prefix = [[0 for _ in range(n)] for _ in range(m)]
        col_incr_stack = defaultdict(list)
        for i in range(m):
            cnt = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    cnt += 1
                else:
                    cnt = 0
                cont_one_cnt_prefix[i][j] = cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                last_idx = i
                ans = max(ans,cont_one_cnt_prefix[i][j])
                while col_incr_stack[j] and col_incr_stack[j][-1][0] >= cont_one_cnt_prefix[i][j]:
                    val, idx = col_incr_stack[j].pop()
                    last_idx = idx
                    ans = max(ans, cont_one_cnt_prefix[i][j] * (i - idx + 1))
                for val, idx in col_incr_stack[j]:
                    ans = max(ans, val * (i - idx + 1))
                col_incr_stack[j].append((cont_one_cnt_prefix[i][j], last_idx))

        return ans
