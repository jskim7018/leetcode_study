def sieve(n):
    if n < 2:
        return []

    # Initialize: True for 2..n-1, False for 0,1
    is_prime = [False, False] + [True] * (n-2)

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Start marking from i*i, not 2*i
            for j in range(i*i, n, i):
                is_prime[j] = False

    # Optional: return the list of primes
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

# Example
print(sieve(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
