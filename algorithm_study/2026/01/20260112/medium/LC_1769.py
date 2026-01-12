from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        f_cnt = 0
        b_cnt = 0

        f_mv_cnt = 0
        b_mv_cnt = 0

        for i in range(n):
            f_mv_cnt += f_cnt
            ans[i] += f_mv_cnt
            if boxes[i] == '1':
                f_cnt += 1

            b_mv_cnt += b_cnt
            ans[-1-i] += b_mv_cnt
            if boxes[-1-i] == '1':
                b_cnt += 1

        return ans
