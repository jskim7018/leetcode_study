from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        if max(nums) == 0:
            return 0

        def sweep(q_end_idx):
            line_sweep = [0]*n
            for q in queries[:q_end_idx+1]:
                line_sweep[q[0]] += q[2]
                if q[1] + 1 < n:
                    line_sweep[q[1] + 1] -= q[2]
            to_dec = 0
            for i in range(n):
                to_dec += line_sweep[i]
                if nums[i] - to_dec > 0:
                    return False
            return True

        sweep(1)
        l = 0
        r = len(queries)-1
        while l <= r:
            print(f'{l}    {r}')
            mid = (l+r)//2
            sweep_result = sweep(mid)
            print(sweep_result)
            if sweep_result:
                r = mid - 1
            else:
                l = mid + 1

        print(l)
        if r + 1 >= len(queries):
            return -1
        else:
            return r + 2
