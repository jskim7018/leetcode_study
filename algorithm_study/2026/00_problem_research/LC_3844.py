class Solution:
    def almostPalindromic(self, s: str) -> int:
        # 사실상 palindrome dp 문제.
        # TODO: O(2 * n^2) => Too slow (원래는 되는게 정상인데 파이썬이라서 안된듯. 의도된 정답일듯.)
        n = len(s)
        is_palindrome = [[[False] * 2 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i][0] = True
            is_palindrome[i][i][1] = True

        longest_palin_len = 1
        longest_alm_palin_len = 1
        for length in range(2, n + 1):  # 2500
            for j in range(length - 1, n):  # 2500
                left = j - (length - 1)
                right = j
                if s[left] == s[j]:
                    if length == 2 or is_palindrome[left + 1][right - 1][0]:
                        longest_palin_len = right - left + 1
                        is_palindrome[left][right][0] = True
                        is_palindrome[left][right][1] = True
                    if length >= 3:
                        is_palindrome[left][right][1] = (is_palindrome[left + 1][right - 2][0]
                                                         or is_palindrome[left + 2][right - 1][0]
                                                         or is_palindrome[left+1][right-1][1])
                    if is_palindrome[left][right][1]:
                        longest_alm_palin_len = right-left+1

        ans = longest_alm_palin_len
        if longest_palin_len + 1 <= n:
            longest_palin_len += 1

        ans = max(ans, longest_palin_len)

        return ans
