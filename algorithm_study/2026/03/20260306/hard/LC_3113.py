from typing import List
from collections import defaultdict
import math


class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        K = int(math.log2(n)) + 1

        self.st = [[0] * n for _ in range(K)]
        self.st[0] = arr[:]

        for k in range(1, K):
            for i in range(n - (1 << k) + 1):
                self.st[k][i] = max(
                    self.st[k - 1][i],
                    self.st[k - 1][i + (1 << (k - 1))]
                )

    def query(self, l, r):
        k = int(math.log2(r - l + 1))
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # 일단 첫번째와 마지막은 같은 숫자여야 함.
        # 사이에는 더 큰 숫자가 없어야 함.
        # 각 숫자별로 독립 처리, max range query해서 max가 되면 계속 누적으로 감.
        # 만약 max가 더 크면 끊고 다시 시작.
        # TODO: Monotonic stack으로 가능.
        n = len(nums)
        num_to_indexes = defaultdict(list)
        for i in range(n):
            num_to_indexes[nums[i]].append(i)

        max_sparse_table = SparseTable(nums)

        ans = 0
        for k, v in num_to_indexes.items():
            curr_cnt = 0

            left = 0
            for idx in v:
                if curr_cnt == 0:
                    left = idx
                right = idx
                ans += 1
                if max_sparse_table.query(left, right) == k:
                    ans += curr_cnt
                    curr_cnt += 1
                else:
                    left = idx
                    curr_cnt = 1
        return ans
