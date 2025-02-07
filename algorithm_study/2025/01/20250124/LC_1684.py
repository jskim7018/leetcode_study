from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_st = set(allowed)

        ans = 0
        for word in words:
            word_st = set(word)

            if word_st.issubset(allowed_st):
               ans += 1

        return ans
