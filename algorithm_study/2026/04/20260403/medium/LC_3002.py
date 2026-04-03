from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        # 두가지 element가 있음.
        # 1. 두 개 모두에 들어있는 element => 어디꺼로 간주하고 넣을지 결정 필요.
        # 2. 1 곳에만 들어있는 element. => 필요하면 그냥 넣음.
        # 1곳만 있는걸로 cap 될때까지 최대한 넣음.
        # 2곳 것으로 나머지를 모두 채워줌.
        n = len(nums1)

        st1 = set(nums1)
        st2 = set(nums2)

        both_st = st1 & st2
        ans = min(n, min(n//2, len(st1 - both_st)) + min(n//2, len(st2-both_st)) + len(both_st))

        return ans
