from typing import List
from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        MAX_PRIME = 100

        counter = Counter(nums)

        is_prime = [True] * (MAX_PRIME+1)
        is_prime[0] = False
        is_prime[1] = False

        for prime in range(2, int(MAX_PRIME ** 0.5) + 1):
            if is_prime[prime]:
                for multiple in range(prime * prime, MAX_PRIME + 1, prime):
                    is_prime[multiple] = False

        for f in counter.values():
            if is_prime[f]:
                return True
        return False
