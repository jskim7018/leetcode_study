from typing import List
from collections import defaultdict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        changed.sort()
        counter = defaultdict(int)
        for c in changed:
            counter[c] += 1
        original = []
        for c in changed:
            if c not in counter:
                continue

            if c*2 in counter:
                original.append(c)
                counter[c * 2] -= 1
                if counter[c*2] == 0:
                    del counter[c * 2]
            else:
                continue
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]

        if len(counter) == 0:
            return original
        else:
            return []
