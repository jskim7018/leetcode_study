from typing import List
from sortedcontainers import SortedSet
import heapq
import time


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = int(1e9+7)

        maxim_prime = max(nums)+1
        is_prime = [True] * (maxim_prime)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2,int(maxim_prime**0.5)+1):
            if is_prime[i]:
                j = 2
                while j*i < maxim_prime:
                    is_prime[j*i] = False
                    j+=1

        def getPrimeCount(number) -> int:
            is_prime_used = set()
            if is_prime[number]:
                return 1
            tmp = number
            for p in range(2, maxim_prime):
                if p*p > number:
                    break
                if tmp % p == 0:
                    if is_prime[tmp//p]:
                        is_prime_used.add(tmp//p)
                    if is_prime[p]:
                        is_prime_used.add(p)
            return len(is_prime_used)

        heap = []
        for i, num in enumerate(nums):
            heap.append((-getPrimeCount(num), i, num)) # max_heap
        heapq.heapify(heap)

        sorted_set = SortedSet()
        sorted_set.add(-1)
        sorted_set.add(len(nums))

        num_to_possible_k_heap = []
        while heap:
            element = heapq.heappop(heap)
            num = element[2]
            idx = element[1]

            sorted_r_index = sorted_set.bisect_right(idx)
            l = sorted_set[sorted_r_index-1]
            r = sorted_set[sorted_r_index]

            possible_k = (r-idx) * (idx-l)
            sorted_set.add(idx)
            num_to_possible_k_heap.append((-num, possible_k))
        heapq.heapify(num_to_possible_k_heap)

        ans = 1
        def fast_exponentiation(base, exponent):
            result = 1
            base = base % MOD  # Ensure base is within mod range

            while exponent > 0:
                if exponent % 2 == 1:  # If exponent is odd, multiply the result
                    result = (result * base) % MOD
                base = (base * base) % MOD  # Square the base
                exponent //= 2  # Divide exponent by 2

            return result

        while k > 0 and num_to_possible_k_heap:
            element = heapq.heappop(num_to_possible_k_heap)
            num = -element[0]
            possible_k = element[1]
            ans *= fast_exponentiation(num, min(possible_k, k))
            ans %= MOD
            k -= possible_k
            if k <= 0:
                break

        return int(ans)
