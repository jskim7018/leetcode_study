from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = []

        prev_diff = nums[1]-nums[0]
        cnt = 2
        for i in range(2, n):
            diff = nums[i] - nums[i-1]

            if diff == prev_diff:
                cnt += 1
            else:
                diffs.append((prev_diff, cnt))
                prev_diff = diff
                cnt = 2
        diffs.append((prev_diff, cnt))

        def get_max_from_diffs(diffs: list[int]) -> int:
            diffs_n = len(diffs)
            ret = 0
            for i in range(diffs_n):
                diff, cnt = diffs[i]

                ret = max(ret, cnt)
                if i + 1 < diffs_n:
                    next_diff, next_cnt = diffs[i+1]
                    ret = max(ret, cnt + 1)
                    if next_cnt == 2 and i + 2 < diffs_n:
                        nnext_diff, nnext_cnt = diffs[i + 2]
                        delta = diff - next_diff
                        nnext_diff += (-delta)
                        if nnext_diff == diff:
                            ret = max(ret, cnt+2)
                            if nnext_cnt == 2 and i + 3 < diffs_n:
                                nnnext_diff, nnnext_cnt = diffs[i+3]
                                if nnnext_diff == diff:
                                    ret = max(ret, cnt+2+nnnext_cnt-1)
            return ret

        ans = get_max_from_diffs(diffs)
        diffs.reverse()
        ans = max(ans, get_max_from_diffs(diffs))
        return ans
