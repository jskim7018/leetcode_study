class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def is_prime(num: int) -> bool:
            if num == 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False

            i = 3
            while i*i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        n = len(s)
        primes_st = set()
        for i in range(n):
            for j in range(i, n):
                num = int(s[i:j+1])
                if is_prime(num):
                    primes_st.add(num)

        primes = list(primes_st)
        primes.sort(reverse=True)

        if len(primes) >= 3:
            return sum(primes[:3])
        else:
            return sum(primes)
