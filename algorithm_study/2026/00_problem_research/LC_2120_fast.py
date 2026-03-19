from typing import List
from collections import defaultdict


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # TODO: O(n)
        m = len(s)

        dR = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
        dC = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

        # Use hashmap instead of array
        limitR = defaultdict(list)
        limitC = defaultdict(list)

        minR = -startPos[0] - 1
        maxR = n - startPos[0]
        minC = -startPos[1] - 1
        maxC = n - startPos[1]

        curR = startPos[0]
        curC = startPos[1]

        res = [None] * m

        for i in range(m):
            # Register triggers
            limitR[curR + minR].append(i)
            limitR[curR + maxR].append(i)
            limitC[curC + minC].append(i)
            limitC[curC + maxC].append(i)

            # Move
            ch = s[i]
            curR += dR[ch]
            curC += dC[ch]

            # Resolve row triggers
            if curR in limitR:
                for start_idx in limitR[curR]:
                    if res[start_idx] is None:
                        res[start_idx] = i - start_idx
                del limitR[curR]

            # Resolve col triggers
            if curC in limitC:
                for start_idx in limitC[curC]:
                    if res[start_idx] is None:
                        res[start_idx] = i - start_idx
                del limitC[curC]

        # Fill remaining
        for i in range(m):
            if res[i] is None:
                res[i] = m - i

        return res