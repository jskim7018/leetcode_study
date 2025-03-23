from typing import List
from collections import defaultdict


# TODO: Editorial 솔루션 분석하기
class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        rows = defaultdict(int)
        cols = defaultdict(int)
        is_row_placed = [False] * n
        is_col_placed = [False] * n
        for rook in rooks:
            rows[rook[0]] += 1
            is_row_placed[rook[0]] = True
            cols[rook[1]] += 1
            is_col_placed[rook[1]] = True


        rows = [(k,v) for k,v in rows.items()]
        cols = [(k,v) for k,v in cols.items()]
        ans = 0
        idx = 0
        rows.sort()
        cols.sort()
        for i, r in rows:
            while r > 1:
                while idx < n and is_row_placed[idx]:
                    idx += 1
                ans += abs(idx-i)
                is_row_placed[idx] = True
                r -= 1
        idx = 0
        for i, c in cols:
            while c > 1:
                while idx < n and is_col_placed[idx]:
                    idx += 1
                ans += abs(idx - i)
                is_col_placed[idx] = True
                c -= 1

        return ans
