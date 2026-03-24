from bisect import bisect_right


class Solution:
    def maxValue(self, events, k):
        events.sort()
        n = len(events)

        starts = [e[0] for e in events]

        # cache binary search results
        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect_right(starts, events[i][1])

        # DP cache
        cache = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i, k_left):
            if i == n or k_left == 0:
                return 0

            if cache[i][k_left] != -1:
                return cache[i][k_left]

            # skip
            skip = dfs(i + 1, k_left)

            # take (NO binary search here anymore)
            take = events[i][2] + dfs(next_idx[i], k_left - 1)

            cache[i][k_left] = max(skip, take)
            return cache[i][k_left]

        return dfs(0, k)