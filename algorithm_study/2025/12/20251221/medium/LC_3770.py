class Solution:
    def largestPrime(self, n: int) -> int:
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False

        # Sieve of Erathosthenes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for mult in range(i*i, n+1, i):
                    is_prime[mult] = False

        primes = [i for i in range(len(is_prime)) if is_prime[i]]

        accum = 0
        ans = 0
        for p in primes:
            accum += p
            if accum > n:
                break
            if is_prime[accum]:
                ans = accum
        return ans
