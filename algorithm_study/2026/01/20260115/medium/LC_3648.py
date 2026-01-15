import math


class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        sensor_coverage = k+k+1

        row_need = math.ceil(m / sensor_coverage)
        col_need = math.ceil(n / sensor_coverage)

        return row_need * col_need
