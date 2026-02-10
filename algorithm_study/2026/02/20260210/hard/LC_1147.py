from collections import deque
import math


class Solution:
    def longestDecomposition(self, text: str) -> int:
        # greedy O(n^2)
        n = len(text)
        left = list()
        right = deque()

        ans = 0
        for i in range(math.ceil(n/2)):
            # rolling hash로 optimize 가능.
            left.append(text[i])
            right.appendleft(text[n-i-1])
            if left == list(right) and i < n-i-1:
                ans += 2
                left.clear()
                right.clear()
        if len(left):
            ans += 1
        return ans
