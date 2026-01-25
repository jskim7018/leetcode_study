from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        s1_n = len(slots1)
        s2_n = len(slots2)

        s1_idx = 0
        s2_idx = 0

        while s1_idx < s1_n and s2_idx < s2_n:
            s1_s, s1_e = slots1[s1_idx]
            s2_s, s2_e = slots2[s2_idx]

            s = max(s1_s, s2_s)
            e = min(s1_e, s2_e)
            if e - s >= duration:
                return [s, s+duration]

            if s1_e >= s2_e:
                s2_idx += 1
            if s2_e >= s1_e:
                s1_idx += 1

        return []