from typing import List
import bisect
from collections import defaultdict


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # binary search?
        # longest subsequence 배열 유지하면서 binary search
        # sorted list로 해결 가능. 숫자에 대해서 최대 길이 각각 저장. 업데이트하면서 나아감.
        incr_mono_stack = []
        idx_to_cnt = defaultdict(int)

        ans = []
        for ob in obstacles:
            idx = bisect.bisect_right(incr_mono_stack, ob)
            if idx < len(incr_mono_stack):
                incr_mono_stack[idx] = ob
            else:
                incr_mono_stack.append(ob)
                idx_to_cnt[len(incr_mono_stack) - 1] = len(incr_mono_stack)
            ans.append(idx_to_cnt[idx])

        return ans
