from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)

        for i in range(m):
            n = len(words[i])
            for j in range(n):
                if j >= m or i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False

        return True
