class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        ones = 0
        l = 0
        ans_len = float('inf')
        ans = ''
        for r in range(n):
            if s[r] == '1':
                ones += 1
            while l <= r and s[l] == '0' or ones > k:
                if s[l] == '1':
                    ones -= 1
                l += 1

            if ones == k:
                candidate = s[l:r+1]
                if len(candidate) < ans_len:
                    ans = candidate
                    ans_len = len(ans)
                elif len(candidate) == len(ans):
                    ans = min(ans, candidate)
                    ans_len = len(ans)
        return ans
