from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 2(2x + y) = tomato slices
        #        y = cheeseSlices - x
        # 2(2x + cheeseSlices-x) = tomato Slices
        # x = (tomatoSlices - 2 cheeseSlices) / 2
        # => x, y는 정수 여야 함. x, y는 음수가 아니어야 함.

        total_jumbo = (tomatoSlices - 2*cheeseSlices) // 2
        if (tomatoSlices - 2*cheeseSlices) % 2 != 0:
            return []
        total_small = cheeseSlices - total_jumbo

        if total_small >= 0 and total_jumbo >= 0:
            return [total_jumbo, total_small]
        else:
            return []

