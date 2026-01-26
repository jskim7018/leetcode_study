from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i: int, j: int) -> int:
            if i == j:
                return 1
            elif i > j:
                return 0

            if s[i] == s[j]:
                ret = dp(i+1, j-1)+2
            else:
                ret = max(dp(i+1, j), dp(i, j-1))

            return ret

        return dp(0, n-1)
