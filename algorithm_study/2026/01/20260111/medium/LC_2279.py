from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needs = [c-r for c,r in zip(capacity,rocks)]
        needs.sort()

        ans = 0
        for need in needs:
            if need <= additionalRocks:
                ans += 1
                additionalRocks -= need
            else:
                break
        return ans
