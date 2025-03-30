
# TODO: Do it in optimized way (longest common substring)
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        def is_palindrome(new_s: str) -> bool:
            for i in range(len(new_s)//2):
                if new_s[i] != new_s[len(new_s)-i-1]:
                    return False
            return True

        ans = 0
        for i in range(m):
            for j in range(i, m+1):
                for k in range(n):
                    for l in range(k, n+1):
                        new_str = s[i:j] + t[k:l]
                        if is_palindrome(new_str):
                            ans = max(ans, len(new_str))

        return ans