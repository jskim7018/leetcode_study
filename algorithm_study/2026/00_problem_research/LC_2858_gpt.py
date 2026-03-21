from collections import defaultdict


class Solution:
    def minEdgeReversals(self, n, edges):
        graph = defaultdict(list)

        # Step 1: build graph
        for u, v in edges:
            graph[u].append((v, 0))  # correct direction
            graph[v].append((u, 1))  # reversed

        # Step 2: compute answer[0]
        def dfs(node, parent):
            total = 0
            for nei, cost in graph[node]:
                if nei == parent:
                    continue
                total += cost + dfs(nei, node)
            return total

        answer = [0] * n
        answer[0] = dfs(0, -1)

        # Step 3: reroot
        def reroot(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                # move root from node -> nei
                if cost == 0:
                    answer[nei] = answer[node] + 1
                else:
                    answer[nei] = answer[node] - 1

                reroot(nei, node)

        reroot(0, -1)
        return answer