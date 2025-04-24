from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        vals_of_node = dict()
        for i in range(len(vals)):
            vals_of_node[i] = []

        for edge in edges:
            vals_of_node[edge[0]].append(vals[edge[1]])
            vals_of_node[edge[1]].append(vals[edge[0]])

        ans = float('-inf')
        for key, vn in vals_of_node.items():
            vn.sort(reverse=True)

            curr_sum = vals[key]
            for i, v in enumerate(vn):
                if i < k and v > 0:
                    curr_sum += v
                else:
                    break
            ans = max(ans, curr_sum)

        return ans
