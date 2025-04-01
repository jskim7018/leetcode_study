from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:

        ans = 0
        row_st = set()
        col_st = set()
        for i in range(len(queries)-1, -1,-1):
            type = queries[i][0]
            idx = queries[i][1]
            val = queries[i][2]

            if type == 0:
                if idx not in row_st:
                    ans += (n-len(col_st))*val
                    row_st.add(idx)
            else:
                if idx not in col_st:
                    ans += (n-len(row_st))*val
                    col_st.add(idx)

        return ans