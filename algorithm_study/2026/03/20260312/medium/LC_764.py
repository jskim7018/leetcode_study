from typing import List
from collections import defaultdict
import bisect


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 이진 탐색으로 구현
        # TODO 이진탐색 없이 dp, min 갱신으로도 가능. one pass로 동시에도 가능.

        row_mines = defaultdict(list)
        col_mines = defaultdict(list)
        mines.sort()
        for x, y in mines:
            row_mines[y].append(x)
        mines.sort(key=lambda e:e[1])
        for x, y in mines:
            col_mines[x].append(y)

        ans = 0
        for i in range(n):
            for j in range(n):
                left = bisect.bisect_right(row_mines[i], j) - 1
                right = bisect.bisect_right(row_mines[i], j)

                if left != -1:
                    left = row_mines[i][left]
                if right < len(row_mines[i]):
                    right = row_mines[i][right]
                else:
                    right = n

                top = bisect.bisect_right(col_mines[j], i) - 1
                bottom = bisect.bisect_right(col_mines[j], i)

                if top != -1:
                    top = col_mines[j][top]
                if bottom < len(col_mines[j]):
                    bottom = col_mines[j][bottom]
                else:
                    bottom = n
                ans = max(ans, min(j-left, right-j, i-top, bottom-i))
        return ans
