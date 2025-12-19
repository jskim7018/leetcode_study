from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowels = set('aeiou')

        vowel_max = 0
        consonant_max = 0

        for v, f in counter.items():
            if v in vowels:
                vowel_max = max(vowel_max, f)
            else:
                consonant_max = max(consonant_max, f)

        return vowel_max + consonant_max
