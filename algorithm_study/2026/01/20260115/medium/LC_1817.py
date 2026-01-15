from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_uam = defaultdict(set)

        for l in logs:
            user_uam[l[0]].add(l[1])

        ans = [0] * k
        for user, uam in user_uam.items():
            ans[len(uam)-1] += 1

        return ans
