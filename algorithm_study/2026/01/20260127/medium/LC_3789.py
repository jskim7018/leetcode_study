class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0
        if costBoth <= cost1 + cost2:
            minim = min(need1, need2)
            need1 -= minim
            need2 -= minim
            ans += costBoth * minim

        if costBoth <= cost1:
            ans += need1 * costBoth
            need2 = max(need2-need1, 0)
            need1 = 0
        if costBoth <= cost2:
            ans += need2 * costBoth
            need1 = max(need1 - need2, 0)
            need2 = 0

        ans += cost1*need1 + cost2 * need2

        return ans
