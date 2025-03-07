from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_primes = [True] * (right+1)
        is_primes[0]= False
        is_primes[1]= False

        i = 2
        while i*i <= right + 1:
            j = 2
            if is_primes[i]:
                while i*j <= right:
                    is_primes[i*j] = False
                    j+=1
            i+=1

        primes = []
        for i in range(left, right+1):
            if is_primes[i]:
                primes.append(i)

        minim = float('inf')
        prime1 = -1
        prime2 = -1
        for i in range(len(primes)-1):
            if minim > primes[i+1]-primes[i]:
                minim = primes[i+1]-primes[i]
                prime1 = primes[i]
                prime2 = primes[i+1]

        return [prime1, prime2]
