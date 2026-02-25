class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(i, j):
            if i < 0:
                return False
            return s[i:j] == s[i:j][::-1]

        dp = [0] * (len(s) + 1)

        for i in range(len(s) + 1):
            dp[i] = dp[i - 1]
            # TODO: 어차피 경우가 2개 (even, odd length palindrome) 뿐임.
            #  (k 사이즈, 그리고 k-1 사이즈. 더 긴것은 볼 필요 없음.)
            if is_palindrome(i - k, i):
                dp[i] = max(dp[i], 1 + dp[i - k])
            if is_palindrome(i - k - 1, i):
                dp[i] = max(dp[i], 1 + dp[i - k - 1])
        return dp[-1]