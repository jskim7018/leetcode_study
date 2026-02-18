from typing import List
from collections import defaultdict

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        # swap graph를 만들 수 있음.
        # swap graph에 속한 애들이 even, odd 둘다면 서로 교환 가능. 즉, even에 max만 넣음.
        n = len(nums)

        graph = defaultdict(list)

        for swap in swaps:
            graph[swap[0]].append(swap[1])
            graph[swap[1]].append(swap[0])

        visited = [False] * n
        def dfs(idx: int) -> List[int]:
            even_cnt = 0
            odd_cnt = 0
            if idx % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

            curr_vals.append((nums[idx], idx))
            for u in graph[idx]:
                if not visited[u]:
                    visited[u] = True
                    nxt_even_cnt, nxt_odd_cnt = dfs(u)
                    even_cnt += nxt_even_cnt
                    odd_cnt += nxt_odd_cnt

            return [even_cnt, odd_cnt]

        ans = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                curr_vals = []
                evens, odds = dfs(i)
                if evens > 0 and odds > 0:
                    curr_vals.sort(reverse=True)
                    for j in range(len(curr_vals)):
                        if j < evens:
                            ans += curr_vals[j][0]
                        else:
                            ans -= curr_vals[j][0]
                else:
                    for j in range(len(curr_vals)):
                        if curr_vals[j][1] % 2 == 0:
                            ans += curr_vals[j][0]
                        else:
                            ans -= curr_vals[j][0]

        return ans
