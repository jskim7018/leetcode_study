class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = []
        for i in range(m):
            new_dp = [set() for _ in range(n)]
            if i == 0:
                new_dp[0].add(grid[i][0])
            for j in range(n):
                if i-1 >= 0:
                    for l in dp[j]:
                        new_dp[j].add(l ^ grid[i][j])
                if j-1 >= 0:
                    for l in new_dp[j-1]:
                        new_dp[j].add(l ^ grid[i][j])
            dp = new_dp

        return min(dp[n-1])
