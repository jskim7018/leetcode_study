# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()

        ans = float('inf')
        for i in range(row):
            l = 0
            r = row-1
            left_most = float('inf')
            while l <= r:
                mid = (l+r)//2
                val = binaryMatrix.get(i, mid)
                if val == 1:
                    left_most = mid
                    r = mid - 1
                else:
                    l = mid + 1
            ans = min(ans, left_most)

        if ans == float('inf'):
            return -1
        else:
            return ans
