class Solution:
    def findRotation(self, mat, target):
        # Don't need to physically actually rotate.
        n = len(mat)

        r0 = True
        r90 = True
        r180 = True
        r270 = True

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    r0 = False
                if mat[i][j] != target[j][n - 1 - i]:
                    r90 = False
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    r180 = False
                if mat[i][j] != target[n - 1 - j][i]:
                    r270 = False

        return r0 or r90 or r180 or r270