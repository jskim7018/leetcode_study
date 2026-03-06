from collections import deque
import bisect


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start = s.count('0')

        if start == 0:
            return 0

        # Distance array
        dist = [-1] * (n + 1)
        dist[start] = 0

        # Two sorted lists for unvisited states
        even = []
        odd = []

        for i in range(n + 1):
            if i == start:
                continue
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        q = deque([start])

        while q:
            m = q.popleft()

            # Compute valid c range
            c1 = max(k - (n - m), 0)
            c2 = min(m, k)

            # Compute resulting interval
            lnode = m + k - 2 * c2
            rnode = m + k - 2 * c1

            # Pick correct parity set
            target_set = even if lnode % 2 == 0 else odd

            # Find first index >= lnode
            idx = bisect.bisect_left(target_set, lnode)

            # Traverse all values <= rnode
            while idx < len(target_set) and target_set[idx] <= rnode:
                nxt = target_set[idx]

                dist[nxt] = dist[m] + 1
                q.append(nxt)

                # Remove visited
                target_set.pop(idx)

            if dist[0] != -1:
                return dist[0]

        return -1