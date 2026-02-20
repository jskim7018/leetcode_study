from typing import List
from collections import defaultdict
import bisect


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # TODO: LIS 공부 확실히 하기. 이거의 핵심 원리 이해하기. LIS 확실히 이해하기.
        def lis(num_list: List[int]) -> int:
            tails = []

            for x in num_list:
                i = bisect.bisect_left(tails, x)
                if i == len(tails):
                    tails.append(x)
                else:
                    tails[i] = x

            return len(tails)

        bit_cnt_by_pos = defaultdict(list)
        for num in nums:
            i = 0
            original_num = num
            # 이진수를 digit (비트) 별로 분해 방법. 10진수와 같은.
            # 그렇다는 것은 8진수 16진수 등 모든 진수 똑같이 적용 가능.
            while num:
                if num % 2:
                    bit_cnt_by_pos[i].append(original_num)
                num //= 2
                i += 1

        ans = 0
        for v in bit_cnt_by_pos.values():
            ans = max(ans, lis(v))
        return ans
