class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # 중복 없이 현재 위치로 까지 했을때 모든 subsequence 갯수.
        mod = 10**9 + 7
        n = len(s)

        dp = [0] * n

        alph_las_pos = dict()
        for i in range(n):
            if s[i] not in alph_las_pos:
                dp[i] = 1
            if i-1 >= 0:
                dp[i] += dp[i-1]
                if s[i] in alph_las_pos and alph_las_pos[s[i]] - 1 >= 0:
                    dp[i] += mod
                    dp[i] -= dp[alph_las_pos[s[i]] - 1]
                dp[i] %= mod

            alph_las_pos[s[i]] = i

            if i - 1 >= 0:
                dp[i] += dp[i-1]
                dp[i] %= mod
        return dp[n-1]
