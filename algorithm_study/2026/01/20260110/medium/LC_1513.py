class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7

        s += '0' # sentinel

        cnt_ones = 0
        ans = 0
        for ch in s:
            if ch == '1':
                cnt_ones += 1
            else:
                ans += (cnt_ones * (cnt_ones+1))//2
                ans %= mod
                cnt_ones = 0
        return ans
