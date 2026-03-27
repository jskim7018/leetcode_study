import random


class Solution:

    def __init__(self, nums):
        self.original = nums[:]  # store original
        self.nums = nums[:]  # working copy

    def reset(self):
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        # Fisher–Yates (Knuth) Shuffle

        arr = self.nums[:]
        n = len(arr)

        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr
