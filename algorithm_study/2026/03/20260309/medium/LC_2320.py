class Solution:
    def countHousePlacements(self, n: int) -> int:
        # dp[i][j] -> j는 집이 있는지 없는지를 알림. i까지했을때 j일때 최대.
        # 2도로는 독립적이기에 하나를 구하고 그것을 곱하면 된다.
        mod = 10**9 + 7

        dp = [[0] * 2 for _ in range(n)]

        have = 1
        not_have = 1

        for i in range(1, n):
            new_have = not_have
            new_not_have = have + not_have

            have = new_have % mod
            not_have = new_not_have % mod

        ans = (have + not_have) % mod
        ans = (ans * ans) % mod

        return ans
