class Solution:
    def countVowels(self, word: str) -> int:
        vowel_st = set('aeiou')

        cnt = 1
        ans = 0
        for i, ch in enumerate(word):
            if ch in vowel_st:
                ans += (len(word) - i) * cnt
            cnt += 1

        return ans
