from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # bfs
        # only need to teleport once fastest.
        n = len(arr)
        num_to_indexes = defaultdict(list)
        for i in range(n):
            num_to_indexes[arr[i]].append(i)

        def bfs() -> int:
            q = deque()

            q.append((0, 0))

            visited = [False] * n
            visited[0] = True
            while q:
                curr_idx, steps = q.popleft()

                if curr_idx == n-1:
                    return steps

                if curr_idx + 1 < n and not visited[curr_idx+1]:
                    visited[curr_idx + 1] = True
                    q.append((curr_idx+1, steps + 1))
                if curr_idx - 1 >= 0 and not visited[curr_idx-1]:
                    visited[curr_idx - 1] = True
                    q.append((curr_idx-1, steps + 1))

                if arr[curr_idx] in num_to_indexes:
                    for idx in num_to_indexes[arr[curr_idx]]:
                        if not visited[idx]:
                            visited[idx] = True
                            q.append((idx, steps + 1))
                    del num_to_indexes[arr[curr_idx]]
            return -1

        return bfs()
