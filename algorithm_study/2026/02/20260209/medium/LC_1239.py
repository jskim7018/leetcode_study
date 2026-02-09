from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 문제의 constraint를 보면 완탐 가능할듯.
        # bitmask 활용 가능할듯. or로 합체, and로 공통 있는지 확인.
        # bit수가 가장 많은 것이 답.
        # 이미 unique 아닌애들 배제.
        unique_bit_arr = []
        for a in arr:
            bitmask = 0
            is_unique = True
            for ch in a:
                ord_ch = ord(ch) - ord('a')
                mask = 1 << ord_ch
                if bitmask & mask != 0:
                    is_unique = False
                    break
                else:
                    bitmask |= mask
            if is_unique:
                unique_bit_arr.append(bitmask)

        n = len(unique_bit_arr)

        def backtrack(idx: int, curr_mask: int) -> int:
            if idx >= n:
                return curr_mask.bit_count()

            ret = backtrack(idx+1, curr_mask)

            if curr_mask & unique_bit_arr[idx] == 0:
                ret = max(ret, backtrack(idx + 1, curr_mask|unique_bit_arr[idx]))

            return ret
        return backtrack(0,0)
