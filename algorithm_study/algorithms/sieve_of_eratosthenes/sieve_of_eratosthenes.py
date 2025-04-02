
# TODO: Study eratosthenes thoroughly
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Assume all numbers are prime initially
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):  # Only check up to √n
        if primes[i]:  # If i is prime
            for j in range(i * i, n + 1, i):  # Mark multiples as non-prime
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]  # Return all primes

# Example Usage
n = 50
print(sieve_of_eratosthenes(n))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, ..., 47]
