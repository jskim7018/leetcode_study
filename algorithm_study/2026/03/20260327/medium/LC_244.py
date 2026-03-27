from typing import List
from collections import defaultdict
import bisect


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indexes = defaultdict(list)
        for i in range(len(wordsDict)):
            self.word_indexes[wordsDict[i]].append(i)
        self.cache = dict()  # frozenset(word1, word2) -> dist

    def shortest(self, word1: str, word2: str) -> int:
        words_set = frozenset([word1, word2])

        if words_set in self.cache:
            return self.cache[words_set]
        ret = float('inf')
        for idx in self.word_indexes[word1]:
            len_w2 = len(self.word_indexes[word2])
            word2_idx = bisect.bisect_right(self.word_indexes[word2], idx)
            if word2_idx < len_w2:
                ret = min(ret, abs(idx - self.word_indexes[word2][word2_idx]))
            if word2_idx-1 >= 0:
                ret = min(ret, abs(idx - self.word_indexes[word2][word2_idx-1]))
        self.cache[words_set] = ret
        return ret

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)