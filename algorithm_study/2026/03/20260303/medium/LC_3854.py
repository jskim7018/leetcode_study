from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        # max, min 각각 모두 변경 가능한지 구함.
        # 둘다 변경 불가시 바로 diff, 변경 가능시 둘다 변경 후 구하기.
        # even으로 시작과 odd으로 시작 2가지 경우를 모두 해봐야 함.

        n = len(nums)

        if n == 1:
            return [0,0]

        def try_parity_alternating(is_diff_parity: bool) -> List[int]:
            _max, _min = max(nums), min(nums)

            is_all_max_change = True
            is_all_min_change = True
            cnt_need_change = 0
            for i in range(n):
                if is_diff_parity ^ (nums[i] % 2 != i % 2):
                    cnt_need_change += 1
                if nums[i] == _max and (is_diff_parity ^ (i % 2 == nums[i] % 2)):
                    is_all_max_change = False
                elif nums[i] == _min and (is_diff_parity ^ (i % 2 == nums[i] % 2)):
                    is_all_min_change = False
            if is_all_min_change:
                _min += 1
            if is_all_max_change:
                _max -= 1
            return [cnt_need_change, abs(_max - _min)]

        ans_cand = [try_parity_alternating(True), try_parity_alternating(False)]
        ans_cand.sort()

        return ans_cand[0]
