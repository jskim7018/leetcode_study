from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        restrict_mapping = {r[0]:r[1] for r in restrictions}

        curr = 0
        arr = [curr]
        for i in range(1, n):
            curr = curr + diff[i-1]
            if i in restrict_mapping:
                max_val = restrict_mapping[i]
                curr = min(curr, max_val)
            arr.append(curr)

        for i in range(n-2, -1, -1):
            d = abs(arr[i] - arr[i+1])
            if d > diff[i]:
                if arr[i+1] > arr[i]:
                    arr[i] = arr[i+1] - diff[i]
                else:
                    arr[i] = arr[i+1] + diff[i]

        return max(arr)
