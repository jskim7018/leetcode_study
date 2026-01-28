from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)

        # TODO: preprocess시에 하나만 사용해도됨.
        prefix_c_dist = [[float('inf')] * n for _ in range(3)]
        suffix_c_dist = [[float('inf')] * n for _ in range(3)]

        for c in range(3):
            for i in range(n):
                pref_curr_c = colors[i]-1
                suff_curr_c = colors[-1-i]-1
                if pref_curr_c == c:
                    prefix_c_dist[c][i] = 0
                elif i-1 >= 0:
                    prefix_c_dist[c][i] = prefix_c_dist[c][i-1] + 1

                if suff_curr_c == c:
                    suffix_c_dist[c][-1-i] = 0
                elif i-1 >= 0:
                    suffix_c_dist[c][-1-i] = suffix_c_dist[c][-1-(i-1)] + 1

        ans = []
        for q in queries:
            idx, c = q[0], q[1] - 1

            minim_dist = min(prefix_c_dist[c][idx], suffix_c_dist[c][idx])
            if minim_dist == float('inf'):
                ans.append(-1)
            else:
                ans.append(minim_dist)

        return ans
