from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.org_nums = nums
        self.shuffled_nums = list(nums)

    def reset(self) -> List[int]:
        return self.org_nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.shuffled_nums)
        return self.shuffled_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()