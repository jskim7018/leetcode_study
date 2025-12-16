class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(sep=" ")

        vowels = set('aeiou')

        base_cnt = 0
        for c in words[0]:
            if c in vowels:
                base_cnt += 1

        ans = words[0]

        for word in words[1:]:
            curr_vowel_cnt = 0
            for c in word:
                if c in vowels:
                    curr_vowel_cnt += 1

            if curr_vowel_cnt == base_cnt:
                word_to_add = "".join(reversed(word))
            else:
                word_to_add = word
            ans += " " + word_to_add

        return ans
