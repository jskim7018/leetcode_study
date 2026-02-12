class Solution:
    def checkPartitioning(self, s: str) -> bool:

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        # palindrome dp -> O(n^2)
        for length in range(2, n):
            for i in range(length-1, n):
                if s[i] == s[i-(length-1)]:
                    if length == 2:
                        is_palindrome[i-(length-1)][i] = True
                    else:
                        is_palindrome[i-(length-1)][i] |= is_palindrome[i-(length-1) + 1][i-1]

        ans = False
        # solve -> O(n^2)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                if is_palindrome[0][i] and is_palindrome[i+1][j] and is_palindrome[j+1][n-1]:
                    ans = True
                    break
        return ans
