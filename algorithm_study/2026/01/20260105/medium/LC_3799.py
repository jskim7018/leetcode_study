from typing import List
from itertools import permutations


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        words_perm = permutations(words, 4)
        ans = []
        for perm in words_perm:
            top = perm[0]
            left = perm[1]
            right = perm[2]
            bottom = perm[3]
            if top[0] == left[0] and top[3] == right[0] \
                and bottom[0] == left[3] and bottom[3] == right[3]:
                ans.append(perm)

        ans.sort(key=lambda x: (x[0],x[1],x[2],x[3]))

        return ans
