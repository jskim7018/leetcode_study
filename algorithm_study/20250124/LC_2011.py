from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0

        for op in operations:
            if '++' in op:
                val += 1
            elif '--' in op:
                val -= 1

        return val
