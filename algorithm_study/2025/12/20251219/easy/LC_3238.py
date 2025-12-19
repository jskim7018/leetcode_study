from typing import List
from collections import defaultdict, Counter


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players_to_balls = defaultdict(Counter)

        st = set()
        for p in pick:
            players_to_balls[p[0]][p[1]] += 1
            if players_to_balls[p[0]][p[1]] > p[0]:
                st.add(p[0])

        return len(st)
