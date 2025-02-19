class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x:float, n: int) -> float:
            if n == -1:
                return 1/x
            if n == 1:
                return x
            if n == 0:
                return 1
            half = int(n/2)
            rem = n % 2
            if n < 0:
                rem = -rem
            ret = pow(x*x, half) * pow(x, rem)
            return ret

        return pow(x,n)
