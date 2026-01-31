from typing import List
from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect_right(letters, target)

        if idx >= len(letters):
            return letters[0]
        else:
            return letters[idx]
