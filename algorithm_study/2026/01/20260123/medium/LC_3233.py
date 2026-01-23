class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(r**0.5)

        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False

        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for j in range(p*p, n+1, p):
                    is_prime[j] = False
        ans = (r-l+1)

        for i in range(int(l**0.5), int(n)+1):
            if is_prime[i]:
                if l <= i*i <= r:
                    ans -= 1

        return ans
