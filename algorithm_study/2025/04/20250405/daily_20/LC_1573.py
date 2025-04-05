import math


class Solution:
    def numWays(self, s: str) -> int:
        MOD = int(1e9 + 7)

        ones_cnt = 0
        for c in s:
            if c == '1':
                ones_cnt += 1
        if ones_cnt == 0:
            ans = math.comb(len(s)-1, 2)
            ans %= MOD
            return ans
        if ones_cnt % 3 != 0:
            return 0

        ones_cnt_per = ones_cnt // 3

        i = 0
        ans = 1
        iteration = 0
        while i < len(s) and iteration < 2:
            cnt_ones = 0
            while i< len(s) and cnt_ones < ones_cnt_per:
                if s[i] == '1':
                    cnt_ones += 1
                i += 1

            cnt_zeros = 0
            while i < len(s) and s[i] != '1':
                cnt_zeros += 1
                i += 1
            ans *= cnt_zeros + 1
            ans %= MOD
            iteration += 1

        return ans
