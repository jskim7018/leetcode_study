from typing import List
import heapq


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        diff_and_costs = [(-abs(c[0]-c[1]), c[0], c[1]) for c in costs]

        diff_and_costs.sort()
        a_cost = 0
        b_cost = 0
        a_cnt = 0
        b_cnt = 0
        for _, a, b in diff_and_costs:
            if a < b and a_cnt < n:
                a_cost += a
                a_cnt += 1
            elif b_cnt < n:
                b_cost += b
                b_cnt += 1
            else:
                a_cost += a
                a_cnt += 1

        return a_cost + b_cost
