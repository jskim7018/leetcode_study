class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        for ch in s:
            if ch == 'i':
                ans = ''.join(reversed(ans))
            else:
                ans += ch
        return ans
