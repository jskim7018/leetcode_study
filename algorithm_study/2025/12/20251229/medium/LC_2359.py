from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_dists_from_node(node: int) -> List[float]:
            curr = node
            dist = 0
            visited = [False] * n
            from_node_dist = [float('inf')] * n
            while True:
                if visited[curr]:
                    break
                visited[curr] = True
                from_node_dist[curr] = dist
                curr = edges[curr]
                if curr != -1:
                    dist += 1
                else:
                    break

            return from_node_dist

        from_node1_dist = get_dists_from_node(node1)
        from_node2_dist = get_dists_from_node(node2)

        minim = float('inf')
        minim_idx = -1
        for i in range(n):
            new_val = max(from_node1_dist[i], from_node2_dist[i])
            if new_val < minim:
                minim = new_val
                minim_idx = i

        return minim_idx
