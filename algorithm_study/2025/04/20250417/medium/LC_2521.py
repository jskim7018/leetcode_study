from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        maxim = max(nums)
        is_prime = [True] * (maxim+1)
        is_prime[0] = False
        is_prime[1] = False

        # Sieve of Eratosthenes
        for prime in range(2, int((maxim)**0.5) + 1):
            j = 2
            if not is_prime[prime]:
                continue
            while j * prime <= maxim:
                is_prime[j*prime] = False
                j += 1

        primes = []
        for i in range(len(is_prime)):
            if is_prime[i]:
                primes.append(i)

        st = set()
        mult = 1
        nums_st = set(nums)
        for num in nums_st:
            mult *= num
        for p in primes:
            if p > mult:
                break
            if mult % p == 0:
                st.add(p)

        return len(st)
