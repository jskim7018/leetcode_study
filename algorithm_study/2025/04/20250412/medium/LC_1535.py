from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxim = max(arr)

        curr = arr[0]
        cnt = 0
        ans = 0
        for num in arr[1:]:
            if curr > num:
               cnt += 1
            else:
                curr = num
                cnt = 1
            if cnt == k or curr == maxim:
                ans = curr
                break
        return ans
