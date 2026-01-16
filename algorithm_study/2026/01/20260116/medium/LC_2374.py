from typing import List
from collections import defaultdict


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        edge_scores = [0]*n

        maxim = 0
        node = -1
        for i in range(n):
            e = edges[i]
            edge_scores[e] += i
            if edge_scores[e] > maxim:
                maxim = edge_scores[e]
                node = e
            elif edge_scores[e] == maxim:
                if node > e:
                    node = e

        return node
