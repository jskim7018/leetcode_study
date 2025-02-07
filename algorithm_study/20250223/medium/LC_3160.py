from typing import List
from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = dict()

        ans = []
        counter = Counter()

        for q in queries:
            if q[0] in balls:
                counter[balls[q[0]]] -= 1
                if counter[balls[q[0]]] == 0:
                    del counter[balls[q[0]]]
            balls[q[0]] = q[1]

            counter[balls[q[0]]] += 1
            ans.append(len(counter))

        return ans
