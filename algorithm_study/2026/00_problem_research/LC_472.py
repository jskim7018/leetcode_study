from typing import List
from functools import cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        st = set(words)

        @cache
        def check_if_possible(s: str, is_init:bool=False) -> bool:
            if s in st and not is_init:
                return True
            ret = False
            for i in range(len(s)-1):
                ret = check_if_possible(s[:i+1]) and check_if_possible(s[i+1:])
                if ret:
                    break
            if ret:
                st.add(s)
            return ret

        ans = []
        for word in words:
            if check_if_possible(word, True):
                ans.append(word)

        return ans
