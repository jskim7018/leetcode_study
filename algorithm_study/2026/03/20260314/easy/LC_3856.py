class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)

        vowels_st = set("aeiou")

        right_idx = n-1

        for i in range(n-1, -1, -1):
            if s[i] in vowels_st:
                right_idx = i-1
            else:
                break

        return s[:right_idx + 1]
