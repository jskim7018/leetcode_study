from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def lcs(idx1, idx2):
            if idx1 >= n or idx2 >= m:
                return 0

            ret = 0
            if word1[idx1] == word2[idx2]:
                ret = lcs(idx1+1, idx2+1) + 1
            else:
                ret = max(lcs(idx1+1, idx2), lcs(idx1, idx2+1))

            return ret

        lcs_ = lcs(0,0)

        return n-lcs_ + m-lcs_