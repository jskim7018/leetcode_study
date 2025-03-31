from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        right_ones_cnt_arr = []

        for i, row in enumerate(grid):
            ones_cnt = 0
            for j in range(n-1, -1, -1):
                if row[j] == 0:
                    ones_cnt += 1
                else:
                    break
            right_ones_cnt_arr.append(ones_cnt)
        ans = 0
        for i in range(n):
            need = n-i-1
            if right_ones_cnt_arr[i] >= need:
                continue
            else:
                isFound = False
                for j in range(i+1, n):
                    if right_ones_cnt_arr[j] >= need:
                        isFound = True
                        for k in range(j-1, i-1, -1):
                            right_ones_cnt_arr[k], right_ones_cnt_arr[k+1] \
                                = right_ones_cnt_arr[k+1], right_ones_cnt_arr[k]
                            ans += 1
                        break
                if not isFound:
                    return -1

        return ans
