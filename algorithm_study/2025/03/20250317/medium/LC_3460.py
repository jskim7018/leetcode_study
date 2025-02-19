class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        canSkip = True
        i = 0
        j = 0
        ans = 0
        while i < n and j < m:
            if s[i] == t[j]:
               ans += 1
               i += 1
               j += 1
            else:
                if canSkip:
                    canSkip = False
                    i += 1
                else:
                    break
        return ans
