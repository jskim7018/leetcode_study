class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        # Precompute factorials up to n
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        def mod_inv(num: int) -> int:
            # fermat's little theorem
            return pow(num, MOD - 2, MOD)

        # Precompute inverse factorials
        inv_fact = [1] * n
        inv_fact[n - 1] = mod_inv(fact[n - 1])
        for i in range(n - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            # n! / k! (n-k)!
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        return (2 * comb(n - 1, k)) % MOD
