from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        # TODO: sort func 만드는게 나을 수도.
        nums.sort(key=lambda x: int(''.join([str(mapping[int(c)]) for c in str(x)])))

        return nums
