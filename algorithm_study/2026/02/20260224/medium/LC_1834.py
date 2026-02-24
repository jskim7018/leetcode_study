from typing import List
import heapq
import pytest


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # heap
        tasks = [(e, p, t_id) for t_id, (e, p) in enumerate(tasks)]
        tasks.sort()
        min_heap = [(tasks[0][1], tasks[0][2],  tasks[0][0])]
        idx = 1
        curr_t = tasks[0][0]
        ans = []
        while min_heap:
            p, t_id, e = heapq.heappop(min_heap)
            ans.append(t_id)
            curr_t = max(curr_t, e)
            curr_t += p
            while idx < len(tasks) and (not min_heap or tasks[idx][0] <= curr_t):
                heapq.heappush(min_heap,
                               (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
                idx += 1
        return ans


@pytest.mark.parametrize("input_tasks, expected", [
    ([[1,2],[2,4],[3,2],[4,1]], [0,2,3,1]),
    ([[7,10],[7,12],[7,5],[7,4],[7,2]], [4,3,2,0,1]),
    ([[1,11]], [0]),
    ([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]],
     [6,1,2,9,4,10,0,11,5,13,3,8,12,7]),
    ([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]], [5,0,1,3,2,4])  # Edge case: when heap is empty but future tasks exist.
])
def test_getOrder(input_tasks, expected):
    sol = Solution()
    assert sol.getOrder(input_tasks) == expected
