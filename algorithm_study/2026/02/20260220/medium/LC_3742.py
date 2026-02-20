from typing import List
from collections import defaultdict, deque


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # dp 가능, bfs 가능
        # Whenever movement is restricted (right/down),
        # DP always beats BFS/relaxation.
        # TODO: Try solving with DP too.
        m, n = len(grid), len(grid[0])

        def bfs() -> int:
            dy = [1, 0]
            dx = [0, 1]

            scores = defaultdict(lambda: -1)

            q = deque()

            q.append(((0,0),k,0))
            ans = -1
            while q:
                (y, x), cost_left, score = q.popleft()

                if score < scores[(y, x, cost_left)]:
                    continue

                if y == m-1 and x == n-1:
                    ans = max(ans, score)

                for i in range(2):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue

                    next_cost_left = cost_left
                    if grid[ny][nx] != 0:
                        next_cost_left -= 1
                    if next_cost_left < 0:
                        continue
                    key = (ny, nx, next_cost_left)
                    next_score = score + grid[ny][nx]
                    if scores[key] < next_score:
                        scores[key] = next_score
                        q.append(((ny, nx), next_cost_left, next_score))
            return ans

        return bfs()

# from typing import List
#
# class Solution:
#     def maxPathScore(self, grid: List[List[int]], k: int) -> int:
#         m, n = len(grid), len(grid[0])
#
#         # dp[i][j][c] = max score reaching (i,j) with cost c
#         dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
#
#         dp[0][0][0] = 0  # start
#
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
#
#                 cell_score = grid[i][j]
#                 cell_cost = 1 if grid[i][j] != 0 else 0
#
#                 for c in range(cell_cost, k + 1):
#                     best = -1
#
#                     # from top
#                     if i > 0 and dp[i - 1][j][c - cell_cost] != -1:
#                         best = max(best, dp[i - 1][j][c - cell_cost] + cell_score)
#
#                     # from left
#                     if j > 0 and dp[i][j - 1][c - cell_cost] != -1:
#                         best = max(best, dp[i][j - 1][c - cell_cost] + cell_score)
#
#                     dp[i][j][c] = best
#
#         ans = max(dp[m - 1][n - 1])
#         return ans if ans != -1 else -1
