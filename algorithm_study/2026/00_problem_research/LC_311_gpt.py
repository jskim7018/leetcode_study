class Solution:
    def multiply(self, mat1, mat2):
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        # Result matrix
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for x in range(k):
                if mat1[i][x] != 0:  # skip zeros
                    for j in range(n):
                        if mat2[x][j] != 0:  # skip zeros
                            res[i][j] += mat1[i][x] * mat2[x][j]

        return res