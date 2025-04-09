class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        curr = 0
        cnt = 0
        for c in reversed(s):
            if c == '0':
               cnt += 1
            else:
                if ((1 << cnt) | curr) <= k:
                    curr |= 1 << cnt
                    cnt += 1
        return cnt
