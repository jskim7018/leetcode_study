class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        prev = ord(s[0]) - ord('a')
        cnt = 1
        n = len(s)
        for i in range(1,n):
            curr = ord(s[i]) - ord('a')
            if prev + 1 == curr:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            prev = curr
        ans = max(ans, cnt)
        return ans
