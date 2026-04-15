from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        if words[startIndex] == target:
            return 0

        for i in range(1, n):
            left = (startIndex - i + n) % n
            right = (startIndex + i) % n

            if words[left] == target or words[right] == target:
                return i

        return -1
