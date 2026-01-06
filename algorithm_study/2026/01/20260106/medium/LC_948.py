from typing import List
from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        dq = deque(tokens)
        n = len(dq)

        l = 0
        r = n-1

        score = 0
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            elif l != r:
                if score > 0:
                    score -= 1
                    power += tokens[r]
                    r -= 1
                else:
                    break
            else:
                break
        return score
