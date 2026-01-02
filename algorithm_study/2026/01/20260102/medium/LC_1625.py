class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        for i in range(10):
            if b % 2 != 1 and i > 0:
                break
            for j in range(10):
                new_s = []
                for k in range(0, len(s), 2):
                    even_digit = (int(s[k]) + i*a) % 10
                    odd_digit = (int(s[k+1]) + j*a) % 10
                    new_s.append(str(even_digit))
                    new_s.append(str(odd_digit))
                new_s = ''.join(new_s)
                for k in range(len(s)):
                    shifted_new_s = new_s[(k*b) % len(s):] + new_s[:(k*b) % len(s)]
                    ans = min(shifted_new_s, ans)
        return ans
