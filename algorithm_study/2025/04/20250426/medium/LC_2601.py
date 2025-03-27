from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        is_primes = [True] * 101
        is_primes[0] = False
        is_primes[1] = False

        for i in range(2, 11):
            j = 2
            if not is_primes[i]:
                continue
            while i*j <= 100:
                is_primes[i*j] = False
                j += 1

        first_prime = -1
        second_prime = -1
        for i, num in enumerate(nums):
            if is_primes[num]:
                if first_prime == -1:
                    first_prime = i
                else:
                    second_prime = i

        if second_prime == -1:
            return 0
        else:
            return abs(second_prime - first_prime)
