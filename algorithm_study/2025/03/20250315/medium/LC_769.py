from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        needList = []
        currList = []
        ans = 0
        for i in range(len(arr)):
            currList.append(arr[i])
            needList.append(i)
            currList.sort()
            if needList == currList:
                ans += 1
                needList.clear()
                currList.clear()

        return ans
