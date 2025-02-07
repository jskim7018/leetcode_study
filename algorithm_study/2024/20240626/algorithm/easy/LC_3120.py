import string

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)

        ans = 0
        for c, C in zip(string.ascii_lowercase, string.ascii_uppercase):
            if c in word_set and C in word_set:
               ans += 1
        return ans
