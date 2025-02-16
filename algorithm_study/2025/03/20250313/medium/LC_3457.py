from typing import List
import math

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort(reverse=True)
        best = math.ceil(n//4/2)
        second_best = math.floor(n//4/2)

        ans = sum(pizzas[:best]) + sum(pizzas[best+1:best+1+second_best*2:2])
        return ans
