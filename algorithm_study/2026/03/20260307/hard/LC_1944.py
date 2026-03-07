from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        decr_stack = []  # height, idx, cnt

        n = len(heights)
        ans = [0] * n
        for i in range(n):
            h = heights[i]
            cnt = 1

            while decr_stack and decr_stack[-1][0] <= h:
                _, popped_idx, popped_cnt = decr_stack.pop()
                ans[popped_idx] = cnt
                cnt = popped_cnt + 1
            decr_stack.append((h,i,cnt))

        cnt = 0
        while decr_stack:
            _, popped_idx, popped_cnt = decr_stack.pop()
            ans[popped_idx] = cnt
            cnt = popped_cnt

        return ans
