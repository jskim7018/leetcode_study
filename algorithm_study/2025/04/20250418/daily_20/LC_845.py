from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        is_decr = False
        is_incr = False

        ans = 0
        cnt = 1
        for i in range(1,n):
            if arr[i-1] < arr[i]:
                if is_decr:
                    ans = max(ans, cnt)
                    cnt = 2
                    is_decr = False
                else:
                    cnt += 1
                is_incr = True
            elif arr[i-1] > arr[i]:
                if is_incr or is_decr:
                    cnt += 1
                    is_incr = False
                    is_decr = True
            else:
                if is_decr:
                    ans = max(ans, cnt)
                    is_decr = False
                is_incr = False
                cnt = 1
        if is_decr:
            ans = max(ans, cnt)
        return ans
