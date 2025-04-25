from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def manhattan_dist(a, b) -> int:
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        heap = []
        heap.append((manhattan_dist(start,target), tuple(target)))

        for road in specialRoads:
            heap.append((manhattan_dist(start, (road[0],road[1]))+road[4], (road[2],road[3])))

        heapq.heapify(heap)
        shortest_dist = defaultdict(lambda:float('inf'))
        while heap:
            popped = heapq.heappop(heap)
            dist = popped[0]
            destination = tuple(popped[1])
            shortest_dist[destination] = dist

            if destination == tuple(target):
                return dist
            heapq.heappush(heap, (dist+manhattan_dist(destination,target), tuple(target)))
            for road in specialRoads:
                next_dist = dist+manhattan_dist(destination, (road[0],road[1]))+road[4]
                if shortest_dist[(road[2],road[3])] > next_dist:
                    shortest_dist[(road[2],road[3])] = next_dist
                    heapq.heappush(heap,
                    (next_dist, (road[2],road[3])))

        return 0
