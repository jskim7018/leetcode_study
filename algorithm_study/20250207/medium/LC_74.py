from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][-1] >= target:
                l = 0
                r = n-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] > target:
                        r = mid-1
                    elif matrix[i][mid] < target:
                        l = mid+1
                    else:
                        return True
                return False
            else:
                continue

        return False
