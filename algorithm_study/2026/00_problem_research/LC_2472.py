class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute palindromes up to length k+1
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, k + 2):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right]:
                    if length == 2:
                        is_palindrome[left][right] = True
                    else:
                        is_palindrome[left][right] = is_palindrome[left + 1][right - 1]

        # dp[i] = max palindromes using first i characters (s[:i])
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # skip current character
            dp[i] = dp[i - 1]

            # check palindrome of length k ending at i-1
            if i - k >= 0 and is_palindrome[i - k][i - 1]:
                dp[i] = max(dp[i], dp[i - k] + 1)

            # check palindrome of length k+1 ending at i-1
            if i - (k + 1) >= 0 and is_palindrome[i - (k + 1)][i - 1]:
                dp[i] = max(dp[i], dp[i - (k + 1)] + 1)

        return dp[n]