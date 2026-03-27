from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    shift_from_j_idx = (j + k + n) % n
                else:
                    shift_from_j_idx = (j - k) % n

                if mat[i][j] != mat[i][shift_from_j_idx]:
                    return False

        return True
