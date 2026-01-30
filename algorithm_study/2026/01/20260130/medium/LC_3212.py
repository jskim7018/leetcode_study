from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        # 항상 최적화 고민 하자. 아래도 preprocessing을 하면서 동시에 답을 구할 수 있다.
        ans = 0
        prev_row_xy_cnt = [[0] * 2 for _ in range(m)]
        for j in range(n):
            curr_x = 0
            curr_y = 0
            for i in range(m):
                if grid[i][j] == 'X':
                    prev_row_xy_cnt[i][0] += 1
                elif grid[i][j] == 'Y':
                    prev_row_xy_cnt[i][1] += 1

                curr_x += prev_row_xy_cnt[i][0]
                curr_y += prev_row_xy_cnt[i][1]
                if curr_x == curr_y and curr_x > 0:
                    ans += 1

        return ans
