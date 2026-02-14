from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 각, query마다 연결된 것들의 LCA 거리 구하는 문제
        # 즉, LCA 문제라고 볼 수 있음.
        # LCA 구하는 것은 n 이기에 시간 복잡도는 O(n*m)
        # 보는 나누기 2 floor로 구하면 됨.

        def lca_total_distance(node1: int, node2: int) -> int:
            node1_ancestors = []
            node2_ancestors = []
            while node1 > 0:
                node1_ancestors.append(node1)
                node1 //= 2
            while node2 > 0:
                node2_ancestors.append(node2)
                node2 //= 2

            n1_idx = 0
            n2_idx = 0

            while (node1_ancestors[n1_idx]
                   != node2_ancestors[n2_idx]):
                if node1_ancestors[n1_idx] > node2_ancestors[n2_idx]:
                    n1_idx += 1
                elif node1_ancestors[n1_idx] < node2_ancestors[n2_idx]:
                    n2_idx += 1
                else:
                    break
            return n1_idx + n2_idx

        ans = []
        for q in queries:
            ans.append(lca_total_distance(q[0], q[1]) + 1)

        return ans
