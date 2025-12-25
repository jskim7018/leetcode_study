from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        for i in range(k):
            curr_happiness = max(0, happiness[i] - i)
            if curr_happiness == 0:
                break
            ans += curr_happiness

        return ans
