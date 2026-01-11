class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_cnt = 0

        tmp_n = n

        a = 1
        first_half_factors = []
        while a <= tmp_n//a:
            if tmp_n % a == 0:
                factor_cnt += 2
                if a == tmp_n // a:
                    factor_cnt -= 1
                first_half_factors.append(a)
            a += 1

        l = 1
        r = factor_cnt

        for factor in first_half_factors:
            if l == k:
                return factor
            elif r == k:
                return n // factor
            l += 1
            r -= 1

        return -1
