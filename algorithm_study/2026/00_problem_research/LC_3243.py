from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # TODO: 자세히 공부 필요.
        curr_shortest = [n - i - 1 for i in range(n)]
        ans = []
        for q in queries:
            prev_path = curr_shortest[q[0]]
            new_path = curr_shortest[q[1]] + 1
            if new_path < prev_path:
                curr_shortest[q[0]] = new_path
                diff = prev_path - new_path
                curr = q[0]-1
                while curr >= 0:
                    if curr_shortest[curr] > prev_path:
                        curr_shortest[curr] -= diff
                    curr -= 1
            ans.append(curr_shortest[0])

        return ans