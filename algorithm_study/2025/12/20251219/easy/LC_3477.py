from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        used = set()

        placed_fruits_cnt = 0
        for f in fruits:
            for idx in range(n):
                if idx in used:
                    continue
                if baskets[idx] >= f:
                    placed_fruits_cnt += 1
                    used.add(idx)
                    break

        return n - placed_fruits_cnt
