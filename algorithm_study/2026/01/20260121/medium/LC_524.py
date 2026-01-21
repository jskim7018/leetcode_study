from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def is_subsequence(word: str) -> bool:
            if len(word) > len(s):
                return False

            w_idx = 0
            for ch in s:
                if ch == word[w_idx]:
                    w_idx += 1
                    if w_idx == len(word):
                        return True
            return False

        ans = ''
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word

        return ans
