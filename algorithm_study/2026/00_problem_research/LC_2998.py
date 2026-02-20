from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # if x <= y then only have choice stay or to increment
        # if x > y then you can do all operations to try to reach y
        # bfs (dp) is possible but is there greedy method thats faster?
        if x <= y:
            return y-x
        # TODO: dfs로 더 빠른 방법 가능. 최대한 각 상황에서 y로 가는 최소한의 방식 사용. (예: 11 or 5로 나누는게 가장 빠름)
        def bfs() -> int:
            q = deque()
            q.append((x, 0))  # curr_x, steps
            curr_minim = float('inf')
            visited = set()
            visited.add(x)
            while q:
                curr_x, steps = q.popleft()
                if steps >= curr_minim:
                    return curr_minim

                if curr_x == y:
                    return steps

                if curr_x % 11 == 0:
                    next_x = curr_x // 11
                    if next_x not in visited:
                        q.append((next_x, steps + 1))
                        visited.add(next_x)
                if curr_x % 5 == 0:
                    next_x = curr_x // 5
                    if next_x not in visited:
                        q.append((next_x, steps + 1))
                        visited.add(next_x)

                if curr_x <= y:
                    curr_minim = min(curr_minim, steps + y - curr_x)
                else:
                    next_x = curr_x - 1
                    if next_x not in visited:
                        q.append((next_x, steps + 1))
                        visited.add(next_x)
                next_x = curr_x + 1
                if next_x not in visited:
                    q.append((next_x, steps + 1))
                    visited.add(next_x)

            return -1

        return bfs()
