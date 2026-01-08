from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_st = set(tuple(map(int, d)) for d in deadends)

        target = tuple(int(t) for t in target)

        def bfs() -> int:
            q = deque()

            start = (0, 0, 0, 0)
            q.append((start, 0))
            visited = set()

            if start in deadends_st:
                return -1
            visited.add(start)

            while q:
                lock, turns = q.popleft()
                if lock == target:
                    return turns

                for i in range(4):
                    for add in (1, -1):
                        lock_list = list(lock)
                        lock_list[i] = (10 + lock_list[i] + add) % 10
                        turned_lock = tuple(lock_list)
                        if turned_lock not in visited and turned_lock not in deadends_st:
                            visited.add(turned_lock)
                            q.append((turned_lock, turns + 1))

            return -1

        return bfs()
