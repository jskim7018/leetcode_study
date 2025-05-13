from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        id = 1
        for building in buildings:
            building.append(id)
            id += 1
        buildings2 = list(buildings)
        mp = defaultdict(int)

        tmp_mp = defaultdict(list)
        tmp_mp2 = defaultdict(list)
        buildings.sort()
        buildings2.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(buildings)):
            b = buildings[i]
            b2 = buildings2[i]
            tmp_mp[b[0]].append((b[1], b[2]))
            tmp_mp2[b2[1]].append((b2[0], b2[2]))

        for v in tmp_mp.values():
            if len(v) >= 3:
                for i in range(1, len(v)-1):
                    mp[v[i][1]] += 1
        for v in tmp_mp2.values():
            if len(v) >= 3:
                for i in range(1, len(v) - 1):
                    mp[v[i][1]] += 1

        ans = 0
        for v in mp.values():
            if v >= 2:
               ans += 1

        return ans
