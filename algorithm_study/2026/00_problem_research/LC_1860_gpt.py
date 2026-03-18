from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        def max_k(diff):
            left, right = 0, int((2 * diff) ** 0.5) + 2
            while left <= right:
                mid = (left + right) // 2
                if mid * (mid + 1) // 2 <= diff:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # Step 1: balance
        if memory1 >= memory2:
            t = max_k(memory1 - memory2)
            memory1 -= t * (t + 1) // 2
        else:
            t = max_k(memory2 - memory1)
            memory2 -= t * (t + 1) // 2

        i = t + 1

        # Step 2: continue simulation (small remaining)
        while True:
            if memory1 >= memory2:
                if memory1 < i:
                    return [i, memory1, memory2]
                memory1 -= i
            else:
                if memory2 < i:
                    return [i, memory1, memory2]
                memory2 -= i
            i += 1
