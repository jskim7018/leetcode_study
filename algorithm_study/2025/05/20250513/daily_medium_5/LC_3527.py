from typing import List
from collections import Counter


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()
        for response in responses:
            counter.update(set(response))

        maxim = 0
        for v in counter.values():
            maxim = max(maxim, v)

        ans = []
        for k, v in counter.items():
            if v == maxim:
                ans.append(k)
        ans.sort()

        return ans[0]
