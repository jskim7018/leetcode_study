class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False

            # 홀수만 확인.
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        s = str(num)

        for i in range(1, len(s) + 1):
            if not is_prime(int(s[:i])):
                return False

        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False

        return True
