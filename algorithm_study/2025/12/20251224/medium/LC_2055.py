from typing import List
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        plate_prefix_sum = [0] * len(s)
        candle_pos = []

        for i, ch in enumerate(s):
            if ch == '|':
                candle_pos.append(i)
            else:
                plate_prefix_sum[i] += 1
            if i > 0:
                plate_prefix_sum[i] += plate_prefix_sum[i-1]

        candle_cnt = len(candle_pos)
        ans = []
        for q in queries:
            left = q[0]
            right = q[1]
            left_most_candle_idx = bisect.bisect_left(candle_pos, left)
            if left_most_candle_idx < candle_cnt and candle_pos[left_most_candle_idx] < left:
                left_most_candle_idx += 1
            right_most_candle_idx = bisect.bisect_left(candle_pos, right)
            if right_most_candle_idx >= candle_cnt or candle_pos[right_most_candle_idx] > right:
                right_most_candle_idx -= 1
            if left_most_candle_idx >= candle_cnt or right_most_candle_idx >= candle_cnt\
                    or candle_pos[left_most_candle_idx] > right \
                    or candle_pos[right_most_candle_idx] < left:
                ans.append(0)
            else:
                ans.append(plate_prefix_sum[candle_pos[right_most_candle_idx]] \
                           - plate_prefix_sum[candle_pos[left_most_candle_idx]])

        return ans
