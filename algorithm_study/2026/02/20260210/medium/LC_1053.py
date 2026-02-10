from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        pivot = -1
        pivot_idx = -1
        maxim = 0
        closest_max_idx = -1

        for i in range(n):
            if i+1 < n and arr[i] > arr[i+1]:
                pivot = arr[i]
                pivot_idx = i
                maxim = arr[i+1]
                closest_max_idx = i+1
            elif pivot > arr[i] > maxim:
                maxim = arr[i]
                closest_max_idx = i
        if closest_max_idx != -1:
            arr[pivot_idx], arr[closest_max_idx] = arr[closest_max_idx], arr[pivot_idx]
        return arr
