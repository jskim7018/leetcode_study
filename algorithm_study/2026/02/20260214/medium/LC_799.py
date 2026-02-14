class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_dp = [poured]

        for i in range(1, query_row+1):
            curr_dp = [0] * (i+1)
            for j in range(len(curr_dp)):
                if j - 1 >= 0:
                    curr_dp[j] += max(0, prev_dp[j-1] - 1) / 2
                if j < len(prev_dp):
                    curr_dp[j] += max(0, prev_dp[j]-1)/2

            prev_dp = curr_dp

        return 1 if prev_dp[query_glass] > 1 else prev_dp[query_glass]
