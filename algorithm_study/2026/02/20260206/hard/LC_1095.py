# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
from functools import cache


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # 이진 탐색 3번.
        # 1. 꼭지점 찾기.
        # 2. 왼쪽, 오른쪽 이진 탐색. 왼쪽에서 먼저 찾으면 끝.
        @cache
        def marr_cache(idx: int) -> int:
            return mountainArr.get(idx)

        n = mountainArr.length()

        l = 0
        r = n-1
        peek = 0
        while l <= r:
            mid = (l+r)//2
            curr_val = marr_cache(mid)
            if mid != 0 and mid != n-1 and marr_cache(mid-1) < curr_val > marr_cache(mid+1):
                peek = mid
                break
            if mid == 0 or marr_cache(mid-1) < curr_val:
                l = mid+1
            elif mid == n-1 or marr_cache(mid+1) < curr_val:
                r = mid-1

        def bin_search(l: int, r: int, is_incr: bool = True) -> int:
            direction = 1 if is_incr else -1
            while l <= r:
                mid = (l + r) // 2
                if marr_cache(mid) == target:
                    return mid
                elif direction*marr_cache(mid) > direction*target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        ans = bin_search(0, peek)
        if ans != -1:
            return ans
        else:
            return bin_search(peek, n-1, False)
