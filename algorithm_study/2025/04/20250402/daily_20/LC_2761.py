from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False

        for prime in range(2,int(n**0.5) + 1):
            if is_prime[prime]:
                for j in range(prime * prime, n + 1, prime):  # Mark multiples as non-prime
                    is_prime[j] = False
        ans = []
        for num in range(2, n//2 + 1):
            if is_prime[num] and is_prime[n-num]:
                ans.append((num ,n-num))

        return ans