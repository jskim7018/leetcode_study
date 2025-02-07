class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        print(vowels)

        str_vowels = []
        for c in s:
            if c in vowels:
                str_vowels.append(c)

        str_vowels.sort()
        vowel_idx = 0
        ans = ""
        for i in range(len(s)):
            if s[i] in vowels:
                ans += str_vowels[vowel_idx]
                vowel_idx += 1
            else:
                ans += s[i]

        return ans
