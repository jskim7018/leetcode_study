from typing import List
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        r = bisect.bisect_left(arr, x)
        l = r-1

        while k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            else:
                diff_l = abs(x-arr[l])
                diff_r = abs(x-arr[r])

                if diff_l <= diff_r:
                    l -= 1
                else:
                    r += 1

            k -= 1

        return arr[l+1:r]
