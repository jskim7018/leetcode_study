from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        curr_cans = []
        chosen = list()
        def backtrack(idx, curr):
            if curr == target:
                chosen.append(tuple(sorted(curr_cans)))
                return
            if idx >= n:
                return
            if curr > target:
                return
            
            already = set()
            for i in range(idx, n):
                if candidates[i] not in already:
                    already.add(candidates[i])
                    curr_cans.append(candidates[i])
                    backtrack(i + 1, curr + candidates[i])
                    curr_cans.pop()


        backtrack(0,0)
        chosen.sort()

        return chosen