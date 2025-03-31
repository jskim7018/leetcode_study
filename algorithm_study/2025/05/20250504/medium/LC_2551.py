from typing import List
import heapq as h


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        # min_flag = 1
        # max_flag = -1
        lst = []

        for i in range(1, n):
            lst.append(weights[i]+weights[i-1])
        lst.sort()

        maxim = sum(lst[len(lst)-(k-1):]) + weights[0] + weights[n-1]
        minim = sum(lst[:k-1]) + weights[0] + weights[n-1]


        return maxim - minim
