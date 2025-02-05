from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        rewards = [(reward1[i], reward2[i], reward1[i]-reward2[i]) for i in range(n)]

        rewards.sort(key=lambda x: x[2], reverse=True)
        ans = 0
        for r in rewards[:k]:
            ans += r[0]

        for r in rewards[k:]:
            ans += r[1]
        return ans
