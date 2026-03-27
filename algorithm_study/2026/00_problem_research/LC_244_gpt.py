from collections import defaultdict


class WordDistance:

    def __init__(self, wordsDict):
        self.pos = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.pos[word].append(i)

    def shortest(self, word1, word2):
        l1 = self.pos[word1]
        l2 = self.pos[word2]

        i = j = 0
        res = float('inf')

        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))

            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1

        return res
