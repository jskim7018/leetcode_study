from collections import defaultdict


class Solution:
    def maxSubstrings(self, word: str) -> int:
        left_most_idx = defaultdict(lambda: -1)

        ans = 0
        for i, ch in enumerate(word):
            if left_most_idx[ch] == -1:
                left_most_idx[ch] = i
            if i - left_most_idx[ch] + 1 >= 4:
                ans += 1
                left_most_idx.clear()

        return ans
