class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 1. dp[i][j] => i에서 시작해서 j개 분해했을때. O(n^2)
        # 2. 해당 dp 안에서 특정 범위의 s가 palindrome인지 확인해야함.
        # 그렇기에 O(n)안에 파악 필요해서 dp로 미리 최소 몇개 필요한지 구함.
        n = len(s)

        dp_palin_need = [[0] * n for _ in range(n)]

        for i in range(n):
            dp_palin_need[i][i] = 0

        for length in range(2, n+1):
            for i in range(length-1, n):
                l = i-(length-1)
                r = i
                if s[l] != s[r]:
                    dp_palin_need[l][r] = 1
                if length >= 3:
                    dp_palin_need[l][r] += dp_palin_need[l+1][r-1]

        dp_main = [[float('inf')] * (k+1) for _ in range(n)]
        for i in range(n):
            dp_main[i][1] = dp_palin_need[0][i]

        for i in range(n):
            for j in range(1, k+1):
                for p in range(i-1, -1, -1):
                    if j-1 >= 0:
                        if dp_main[p][j - 1] == float('inf'):
                            break
                        dp_main[i][j] = min(dp_main[i][j], dp_main[p][j-1] + dp_palin_need[p+1][i])

        return dp_main[n-1][k]
