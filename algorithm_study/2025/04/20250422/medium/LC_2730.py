class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        repetitive_cnt = 0
        l = 0

        ans = 1
        for r in range(1, n):
            if s[r] == s[r-1]:
                repetitive_cnt += 1

            while l+1 < r and repetitive_cnt > 1:
                if s[l] == s[l+1]:
                    repetitive_cnt -= 1
                l += 1
            ans = max(ans, r-l + 1)

        return ans
