class Solution:
    def smallestValue(self, n: int) -> int:
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                j = i*i
                while j <= n:
                    is_prime[j] = False
                    j += i

        primes = [p for p in range(len(is_prime)) if is_prime[p]]

        prev_n = n
        while True:
            prime_factors = []
            curr_p_idx = 0
            while n > 1:
                if n % primes[curr_p_idx] == 0:
                    prime_factors.append(primes[curr_p_idx])
                    n //= primes[curr_p_idx]
                else:
                    curr_p_idx += 1
            n = sum(prime_factors)
            if len(prime_factors) <= 1 or n == prev_n:
                break
            prev_n = n
        return n
