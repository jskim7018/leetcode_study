from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def bin_reflection(num: int) -> int:
            bin_of_num = bin(num)[2:]
            return int(''.join(reversed(bin_of_num)))

        items = [(num, bin_reflection(num)) for num in nums]

        items.sort(key=lambda x:(x[1], x[0]))

        return [num for num, bin_refl in items]
