class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        vowel_st = set('aeiou')
        vowels = ['a', 'e', 'i', 'o', 'u']

        ans = 0
        i = 0
        while i < n:
            if word[i] == 'a':
                v_idx = 0
                j = i + 1
                while j < n:
                    if word[j] in vowel_st:
                        if v_idx + 1 < 5 and vowels[v_idx+1] == word[j]:
                            v_idx += 1
                        elif vowels[v_idx] != word[j]:
                            break
                    if v_idx == 4:
                        ans = max(ans, j - i + 1)
                    j += 1
                i = j - 1
            i += 1

        return ans
