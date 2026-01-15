from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        final_shift = [0] * n

        for i in range(n - 1, -1, -1):
            final_shift[i] = shifts[i]
            if i + 1 < n:
                final_shift[i] += final_shift[i+1]

            final_shift[i] %= 26

        def shift(ch: str, x: int) -> str:
            shifted_ch = chr((ord(ch) - ord('a') + x) % 26 + ord('a'))
            return shifted_ch

        ans = [shift(s[i], final_shift[i]) for i in range(n)]

        return ''.join(ans)
