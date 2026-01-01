from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        search_base = set(wordlist)
        search_cap = dict()
        search_vowel = dict()

        for word in wordlist:
            word_lower = word.lower()
            word_no_vowel = ''.join('_' if c.lower() in 'aeiou' else c.lower() for c in word)

            if word_lower not in search_cap:
                search_cap[word_lower] = word
            if word_no_vowel not in search_vowel:
                search_vowel[word_no_vowel] = word

        ans = []
        for q_word in queries:
            q_vowel_word = ''.join('_' if c.lower() in 'aeiou' else c.lower() for c in q_word)

            if q_word in search_base:
                ans.append(q_word)
            elif q_word.lower() in search_cap:
                ans.append(search_cap[q_word.lower()])
            elif q_vowel_word in search_vowel:
                ans.append(search_vowel[q_vowel_word])
            else:
                ans.append("")

        return ans
