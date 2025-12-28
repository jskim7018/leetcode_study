from typing import List
from itertools import groupby
from functools import cache


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        word_to_group = list(zip(words, groups))

        def calc_hamming_dist(word1: str, word2: str) -> int:
            cnt = 0
            for c1, c2 in zip(word1,word2):
                if c1 != c2:
                    cnt += 1
            return cnt

        @cache
        def longest_subsequence(idx: int) -> int:
            nonlocal child

            ret = 1
            for i in range(idx+1, len(word_to_group)):
                if len(word_to_group[idx][0]) == len(word_to_group[i][0]) and \
                        calc_hamming_dist(word_to_group[idx][0], word_to_group[i][0]) == 1 and \
                        word_to_group[idx][1] != word_to_group[i][1]:
                    tmp = 1 + longest_subsequence(i)
                    if ret < tmp:
                        ret = tmp
                        child[idx] = i
            return ret

        maxim = 0
        child = [-1] * len(word_to_group)
        for i in range(len(word_to_group)):
            maxim = max(maxim, longest_subsequence(i))

        ans = []
        _next = -1
        is_max_found = False

        for i in range(len(word_to_group)):
            if maxim == 0:
                break
            if i == _next:
                ans.append(word_to_group[i][0])
                _next = child[i]
            elif longest_subsequence(i) == maxim and not is_max_found:
                ans.append(word_to_group[i][0])
                _next = child[i]
                is_max_found = True

        return ans
