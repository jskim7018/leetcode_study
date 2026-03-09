class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # 모든 경우에 안되는 경우들을 모두 뺀다.
        # dp[i][j][k] -> i 현재 위치, j 남은 one_갯수, k 같은 것 연속 갯수, l 마지막 0 혹은 1
        mod = 10**9 + 7

        dp0 = [[0] * (one+1) for _ in range(zero+1)]
        dp1 = [[0] * (one+1) for _ in range(zero+1)]
        for i in range(1, min(one, limit)+1):
            dp1[0][i] = 1
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1

        for i in range(1, zero+1):
            for j in range(1, one+1):
                for k in range(1, limit+1):
                    is_over = True
                    if i-k >= 0:
                        is_over = False
                        dp0[i][j] += dp1[i-k][j]
                    dp0[i][j] %= mod
                    if j-k >= 0:
                        is_over = False
                        dp1[i][j] += dp0[i][j-k]
                    dp1[i][j] %= mod
                    if is_over:
                        break

        return (dp0[zero][one] + dp1[zero][one]) % mod
