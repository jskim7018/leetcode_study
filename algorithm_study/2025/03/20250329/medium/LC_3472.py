from functools import cache


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        @cache
        def solve(i,j,k) -> int:
            if i == j:
                return 1
            if i > j:
                return 0
            need = min(abs(ord(s[i])-ord(s[j])), 26-abs(ord(s[i])-ord(s[j])))
            ret = 0
            if need <= k:
                ret += solve(i+1, j-1, k-need) + 2
            ret = max(ret, solve(i+1, j, k))
            ret = max(ret, solve(i, j-1, k))

            return ret
        ans = solve(0, len(s)-1, k)
        solve.cache_clear()
        return ans

