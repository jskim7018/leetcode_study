class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_vowels = [c for c in s if c in vowels]
        rev_s_vowels = s_vowels[::-1]

        curr_v_idx = 0
        ans = ""
        for i in range(len(s)):
            if s[i] in vowels:
                ans += rev_s_vowels[curr_v_idx]
                curr_v_idx += 1
            else:
                ans += s[i]
        return ans

# Two-pointer로도 가능할듯.