from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        n = len(s)

        for i in range(n//2):
            s[i], s[-1-i] = s[-1-i], s[i]

        start = 0
        word_len = 0
        for i in range(n):
            if s[i] != ' ':
                word_len += 1
            if s[i] == ' ' or i == n-1:
                for j in range(word_len//2):
                    s[start+j], s[(start + word_len - 1)-j] = s[(start + word_len - 1)-j], s[start+j]
                word_len = 0
                start = i + 1
