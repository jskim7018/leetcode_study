class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        l = 0
        r = n-1

        while l < r:
            if s[l] == s[r]:
                ch = s[l]
                while l <= r and s[l] == ch:
                    l += 1
                while l <= r and s[r] == ch:
                    r -= 1
            else:
                break
        return r-l+1
