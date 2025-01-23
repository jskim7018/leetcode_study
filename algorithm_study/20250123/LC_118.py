class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1]]

        for i in range(1, numRows):
            row = []
            for j in range(i+1):
                val = 0
                if i > 0:
                    if j-1 >= 0:
                        val += pascals[i-1][j-1]
                    if j < len(pascals[i-1]):
                        val += pascals[i-1][j]
                row.append(val)
            pascals.append(row)
        return pascals
