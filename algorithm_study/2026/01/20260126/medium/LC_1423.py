from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        suffix_sum = list(cardPoints)

        for i in range(1, n):
            suffix_sum[-1-i] += suffix_sum[-1-i+1]

        ans = 0
        prefix_sum = 0
        for i in range(k+1):
            curr = prefix_sum
            suffix = k - i
            if suffix > 0:
                curr += suffix_sum[-1-(suffix-1)]
            ans = max(ans, curr)

            if i < len(cardPoints):
                prefix_sum += cardPoints[i]

        return ans
