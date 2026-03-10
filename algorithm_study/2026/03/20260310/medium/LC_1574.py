from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 3가지 경우. 왼쪽이 비거나, 가운데가 비거나, 오른쪽이 비거나.
        # suffix 만들어서 계산해두고 가능한 index를 구함.
        n = len(arr)

        suffix_non_dec_start_idx = n-1
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[i+1]:
                suffix_non_dec_start_idx = i
            else:
                break

        ans = suffix_non_dec_start_idx
        curr_suffix_idx = suffix_non_dec_start_idx
        for i in range(n):
            if i-1 >= 0 and arr[i] < arr[i-1]:
                break

            while curr_suffix_idx < n and arr[i] > arr[curr_suffix_idx]:
                curr_suffix_idx += 1

            ans = min(ans, max(0, (curr_suffix_idx-1) - (i+1) + 1))

        return ans
