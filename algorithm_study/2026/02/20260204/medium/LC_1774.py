from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        baseCosts.sort()

        all_toppings = toppingCosts * 2

        n = len(all_toppings)

        possible_set = set(baseCosts)
        curr_best = float('inf')
        for base in baseCosts:
            if abs(target-curr_best) == abs(target-base):
                if curr_best > base:
                    curr_best = base
            elif abs(target-curr_best) > abs(target-base):
                curr_best = base

        for idx in range(n):
            new_possible = set()
            for poss in possible_set:
                new = poss+all_toppings[idx]
                if abs(target - curr_best) > abs(target - new):
                    curr_best = new
                    new_possible.add(new)
                elif abs(target - curr_best) == abs(target - new):
                    if curr_best > new:
                        curr_best = new
                        new_possible.add(new)
                elif new <= target:
                    new_possible.add(new)
            possible_set.update(new_possible)
        return curr_best

