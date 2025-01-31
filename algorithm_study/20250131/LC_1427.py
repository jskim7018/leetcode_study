from typing import List
from collections import deque

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_by = 0
        for sh in shift:
            if sh[0] == 0:
                shift_by -= sh[1]
            else:
                shift_by += sh[1]

        shift_by %= len(s)

        if shift_by >= 0:
            return s[len(s)-shift_by:len(s)]+s[0:len(s)-shift_by]
        if shift_by < 0:
            return s[-shift_by:len(s)] + s[0:-shift_by]
