from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7

        m, n = len(board), len(board[0])

        def solve() -> List[int]:
            dp = [[float('-inf')] * n for _ in range(m)]
            dp_ways = [[0] * n for _ in range(m)]
            dp[0][0] = 0
            dp_ways[0][0] = 1
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'X':
                        continue
                    curr_val = 0
                    if board[i][j].isdigit():
                        curr_val = int(board[i][j])
                    curr_maxim = dp[i][j]
                    if i-1 >= 0 and j - 1 >= 0:
                        curr_maxim = max(curr_maxim, dp[i-1][j-1] + curr_val)
                    if i-1 >= 0:
                        curr_maxim = max(curr_maxim, dp[i-1][j] + curr_val)
                    if j - 1 >= 0:
                        curr_maxim = max(curr_maxim, dp[i][j-1] + curr_val)

                    if i-1 >= 0 and j - 1 >= 0:
                        if dp[i-1][j-1] + curr_val == curr_maxim:
                            dp_ways[i][j] += dp_ways[i-1][j-1]
                    if i-1 >= 0:
                        if dp[i - 1][j] + curr_val == curr_maxim:
                            dp_ways[i][j] += dp_ways[i - 1][j]
                    if j - 1 >= 0:
                        if dp[i][j - 1] + curr_val == curr_maxim:
                            dp_ways[i][j] += dp_ways[i][j - 1]
                    dp[i][j] = curr_maxim
                    dp_ways[i][j] %= mod

            if dp[m-1][n-1] == float('-inf'):
                return [0, dp_ways[m-1][n-1]]
            else:
                return [int(dp[m-1][n-1]), dp_ways[m-1][n-1]]

        return solve()
