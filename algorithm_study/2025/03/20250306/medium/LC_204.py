import math


class Solution:
    def countPrimes(self, n: int) -> int:

        # Sieve of Era.
        prime_candidates = [False, False] + [True]*(n-2)

        for i in range(2, int(math.sqrt(n)) + 1):
            if prime_candidates[i]:
                for multiple in range(i*i, n, i):
                    prime_candidates[multiple] = False
        return sum(prime_candidates)
