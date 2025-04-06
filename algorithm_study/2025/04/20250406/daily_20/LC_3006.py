from typing import List
import bisect


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        a_indexes = [i for i in range(len(s)) if s.startswith(a, i)]
        b_indexes = [i for i in range(len(s)) if s.startswith(b, i)]

        b_indexes.sort()
        ans = []
        for index in a_indexes:
            left = bisect.bisect_left(b_indexes, index)-1
            right = bisect.bisect_left(b_indexes, index)

            if len(b_indexes) == 0:
                continue
            if (left >= 0 and b_indexes[left] >= index-k) or \
                (right < len(b_indexes) and b_indexes[right] <= index+k):
                ans.append(index)

        return ans
