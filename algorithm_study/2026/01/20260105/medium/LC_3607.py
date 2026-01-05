from typing import List
from collections import defaultdict
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for con in connections:
            u = con[0]
            v = con[1]
            graph[u].append(v)
            graph[v].append(u)

        def dfs(v: int, group_id: int):
            power_grid_group[group_id].append(v)
            station_to_group_id[v] = group_id
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    dfs(u, group_id)

        power_grid_group = defaultdict(list)
        station_to_group_id = defaultdict(int)
        group_id = 1
        visited = [False] * (c+1)
        for i in range(1, c+1):
            if visited[i]:
                continue
            visited[i] = True
            dfs(i, group_id)
            heapq.heapify(power_grid_group[group_id])
            group_id += 1

        offline_stations = set()
        ans = []
        for q in queries:
            command = q[0]
            station = q[1]
            if command == 1:
                if station not in offline_stations:
                    ans.append(station)
                else:
                    alive_stations = power_grid_group[station_to_group_id[station]]
                    while alive_stations:
                        if alive_stations[0] not in offline_stations:
                            ans.append(alive_stations[0])
                            break
                        else:
                            heapq.heappop(alive_stations)
                    if not alive_stations:
                        ans.append(-1)
            elif command == 2:
                offline_stations.add(station)

        return ans
