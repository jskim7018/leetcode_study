from typing import List
import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)

        maxim = max(nums)

        is_primes = [True] * (maxim + 1)
        is_primes[0] = False
        is_primes[1] = False
        for i in range(2, int(maxim**0.5)+1):
            j = 2
            if not is_primes[i]:
                continue
            while i * j <= maxim:
                is_primes[i * j] = False
                j += 1


        primes = []
        for i in range(maxim + 1):
            if is_primes[i]:
                primes.append(i)
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i+1]:
                diff = nums[i] - nums[i + 1] + 1
                greater_prime_idx = bisect.bisect_left(primes, diff)
                if greater_prime_idx >= len(primes) or primes[greater_prime_idx] >= nums[i]:
                    return False
                else:
                    nums[i] -= primes[greater_prime_idx]
        return True
