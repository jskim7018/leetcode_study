class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = int(1e9)+7

        even_digit_cnt = 5
        prime_digit_cnt = 4

        even_cnt = n//2 + n % 2
        odd_cnt = n//2

        def fast_mod_exp(base: int, exponent: int, mod: int) -> int:
            result = 1
            base = base % mod

            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exponent //= 2

            return result

        ans = (fast_mod_exp(even_digit_cnt, even_cnt, MOD) *
               fast_mod_exp(prime_digit_cnt, odd_cnt, MOD))
        ans %= MOD

        return ans
