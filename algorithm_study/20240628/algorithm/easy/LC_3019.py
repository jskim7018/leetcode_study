class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        s = s.lower()

        for i in range(0, len(s)-1):
            if s[i] != s[i+1]:
                ans += 1
        return ans
