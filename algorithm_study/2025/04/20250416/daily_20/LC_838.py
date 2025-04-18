from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        curr = [(d, 0) for d in dominoes]
        def bfs():
            queue = deque()
            for i, c in enumerate(dominoes):
                if c == 'R':
                    queue.append((c,i+1,1))
                elif c == 'L':
                    queue.append((c,i-1,1))

            while queue:
                popped = queue.popleft()
                dir = popped[0]
                idx = popped[1]
                step = popped[2]
                if idx < 0 or idx >= len(dominoes):
                    continue

                if curr[idx][0] == '.' and curr[idx][1] == 0:
                    curr[idx] = (dir, step)
                else:
                    if curr[idx][1] > step:
                        curr[idx] = (dir, step)
                    elif curr[idx][1] == step:
                        curr[idx] = ('.', 0)
                    else:
                        continue

                n_idx = ''
                if dir == 'L':
                    n_idx = idx - 1
                elif dir == 'R':
                    n_idx = idx + 1
                queue.append((dir, n_idx, step+1))

        bfs()

        return ''.join([x for x, _ in curr])
