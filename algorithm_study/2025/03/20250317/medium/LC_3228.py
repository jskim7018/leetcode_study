class Solution:
    def maxOperations(self, s: str) -> int:
        ones_cnt = 0

        ans = 0
        isPrevOne = False
        for c in s:
            if c == '1':
                ones_cnt += 1
                isPrevOne = True
            if c == '0' and isPrevOne:
                ans += ones_cnt
                isPrevOne = False

        return ans
