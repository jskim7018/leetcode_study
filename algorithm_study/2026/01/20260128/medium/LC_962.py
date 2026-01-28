from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # decreasing monotonic stack + binary search
        # binary search도 필요 없음.
        # TODO: monotonic stack을 만들고 그다음 맨 뒤에서 부터 하나씩 하면 최적이 보장됨.
        stck = []
        ans = 0
        for i, num in enumerate(nums):
            if not stck:
                stck.append((num, i))
            else:
                if stck[-1][0] > num:
                    stck.append((num, i))
                else:
                    l = 0
                    r = len(stck)-1
                    smaller_idx = -1
                    while l <= r:
                        mid = (l+r)//2
                        if stck[mid][0] <= num:
                            smaller_idx = mid
                            r = mid - 1
                        else:
                            l = mid + 1
                    if smaller_idx != -1:
                        ans = max(ans, i - stck[smaller_idx][1])
        return ans
