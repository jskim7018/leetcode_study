class Solution:
    def removeVowels(self, s: str) -> str:
        vowel_st = set("aeiou")

        new_str = ""
        for c in s:
            if c not in vowel_st:
                new_str += c

        return new_str
