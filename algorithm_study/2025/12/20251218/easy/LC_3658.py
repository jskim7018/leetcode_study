class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def seq_sum(n) -> int:
            return (n*(n+1))//2

        # gcd 구하는 법 확실히 익히는 것 중요할듯.
        def _gcd(a, b) -> int:
            if b == 0:
                return a
            return _gcd(b, a%b)

        sum_even = seq_sum(n) * 2
        sum_odd = seq_sum(n-1) * 2 + n

        return _gcd(sum_even, sum_odd)
