from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window
        # 오른쪽으로 될때까지 r 확장 (클때는)
        # 만약 작으면 l,r 모두 이동.
        # 계속 되면 맨 처음으로 되었던곳

        # k와 and가 되는 구간들만 처리.
        # bit별로 가장 처음으로 1이었던 위치를 저장, 단 뒤에서 0이 나오면 -1으로.
        def count_subarrays(l: int, r: int):
            first_bit_idx = defaultdict(lambda: -1)
            ret = 0
            for i in range(l, r+1):
                bits_to_check = nums[i] - k
                minim_idx = i+1
                for curr_bit_pos in range(32):
                    bit = (bits_to_check >> curr_bit_pos) & 1
                    if bit == 1:
                        if first_bit_idx[curr_bit_pos] == -1:
                            first_bit_idx[curr_bit_pos] = i
                        minim_idx = min(minim_idx, first_bit_idx[curr_bit_pos])
                    elif first_bit_idx[curr_bit_pos] != -1:
                        first_bit_idx[curr_bit_pos] = -1
                ret += minim_idx-l
            return ret

        n = len(nums)
        i = 0
        ans = 0
        while i < n:
            if nums[i] & k != k:
                i += 1
                continue
            left = i
            right = i
            while i < n and nums[i] & k == k:
                right = i
                i += 1
            ans += count_subarrays(left, right)
            i += 1

        return ans
