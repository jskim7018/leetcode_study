from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m, n = len(votes), len(votes[0])
        counter = defaultdict(list)
        cands = set()
        for v in votes:
            for c in v:
                cands.add(c)
        for j in range(n):
            curr_counter = defaultdict(int)
            for i in range(m):
                curr_counter[votes[i][j]] += 1

            for a in cands:
                counter[a].append(curr_counter[a])

        sort_votes = []
        for k, v in counter.items():
            sort_votes.append(v + [k])
        sort_votes.sort(key=lambda x: ([-a for a in x[:-1]], x[-1]))

        return ''.join([x[-1] for x in sort_votes])
