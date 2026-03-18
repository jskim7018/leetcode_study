from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        curr_bits = 1

        ans = 1
        while memory1 >= curr_bits or memory2 >= curr_bits:
            if memory1 >= memory2:
                memory1 -= curr_bits
            else:
                memory2 -= curr_bits
            curr_bits += 1

            ans = curr_bits

        return [ans, memory1, memory2]
