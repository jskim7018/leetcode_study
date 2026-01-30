

class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [1, 2, 6]

        dp = [0] * (n+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, n+1):
                dp[i] += dp[i-c]
                dp[i] %= mod

        # 4- 1개, 2개인 경우를 추가 한다. 거꾸로 가서 딱 2 경우만 추가 되도록 한다.
        # 밑에 식을 잘 보면 n에는 한번만 dp[i-4]와 dp[i-8]을 더해준다.
        # for i in range(n, -1, -1):
        #     if i-4 >= 0:
        #         dp[i] += dp[i-4]
        #     if i-8 >= 0:
        #         dp[i] += dp[i-8]
        #     dp[i] %= mod
        if n-4 >= 0:
            dp[n] += dp[n - 4]
        if n-8 >= 0:
            dp[n] += dp[n-8]

        return dp[n] % mod
