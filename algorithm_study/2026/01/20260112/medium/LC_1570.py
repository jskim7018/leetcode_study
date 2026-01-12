from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vec = dict()
        for i, num in enumerate(nums):
            self.sparse_vec[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k, v in self.sparse_vec.items():
            ans += v * vec.sparse_vec[k]
        return ans
