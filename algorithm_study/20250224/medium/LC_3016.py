from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        counter = counter.most_common()

        ans = 0
        for i in range(len(counter)):
            ans += (i//8 + 1) * counter[i][1]
        return ans
