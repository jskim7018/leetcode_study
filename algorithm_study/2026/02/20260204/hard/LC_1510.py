class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)

        for i in range(1, len(dp)):
            num = 1
            while i - num*num >= 0:
                if not dp[i-num*num]:
                    dp[i] = True
                    break
                num += 1

        return dp[n]
