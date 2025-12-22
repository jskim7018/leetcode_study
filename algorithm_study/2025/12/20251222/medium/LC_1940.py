from typing import List


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)

        ans = []

        arr_pointers = [0] * n

        is_done = False
        while not is_done:
            curr_max = 0
            for i in range(n):
                if arr_pointers[i] >= len(arrays[i]):
                    is_done = True
                    break
                curr_max = max(curr_max, arrays[i][arr_pointers[i]])
            if is_done:
                break
            cnt = 0
            for i in range(n):
                while arrays[i][arr_pointers[i]] < curr_max:
                    arr_pointers[i] += 1
                    if arr_pointers[i] >= len(arrays[i]):
                        is_done = True
                        break
                if is_done:
                    break
                else:
                    if arrays[i][arr_pointers[i]] == curr_max:
                        cnt += 1
                        arr_pointers[i] += 1
            if cnt == n:
                ans.append(curr_max)
        return ans
