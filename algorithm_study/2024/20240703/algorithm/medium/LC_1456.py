from collections import Counter

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        vowel_cnt = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_cnt += 1
        ans = vowel_cnt

        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                vowel_cnt -= 1
            if s[i+k-1] in vowels:
                vowel_cnt += 1
            ans = max(ans, vowel_cnt)
        return ans
