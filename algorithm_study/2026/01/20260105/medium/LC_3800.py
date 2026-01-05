class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        # flip 2번 vs (swap 1번) vs (cross 1번 + swap 1번)
        n = len(s)

        s_ones = 0
        s_zeroes = 0

        for i in range(n):
            if s[i] != t[i]:
                if s[i] == '0':
                    s_zeroes += 1
                else:
                    s_ones += 1

        ans = 0

        minim = min(s_ones, s_zeroes)
        s_ones -= minim
        s_zeroes -= minim
        if swapCost < flipCost * 2:
            ans += swapCost * minim
        else:
            ans += flipCost * minim * 2
        maxim = max(s_ones, s_zeroes)
        if maxim % 2 == 1:
            maxim -= 1
            ans += flipCost

        if swapCost + crossCost < flipCost * 2:
            ans += (swapCost+crossCost) * maxim//2
        else:
            ans += flipCost * maxim

        return ans
