from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        groups = set()
        groups2 = set()
        for word in words:
            if len(word) < k:
                continue
            prefix = word[:k]
            if prefix in groups:
                if prefix not in groups2:
                    groups2.add(prefix)
            else:
                groups.add(prefix)

        return len(groups2)
