from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)

        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if words[i] != words[j]:
                    ans = max(ans, j-i+1)
        return ans
