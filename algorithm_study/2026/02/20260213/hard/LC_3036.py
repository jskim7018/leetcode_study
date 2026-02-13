from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # kmp/lps랑 느낌이 비슷함.
        # lps의 방식을 활용하는 문제인듯.
        # lps/string search 방식 맞는 듯.
        # (nums릉 패턴 배열로 변경할 수 있음), 그 다음 pattern이 nums에서 몇개있는지 파악.

        # The time complexity of building the LPS array is O(n)
        def compute_lps(pattern: List[int]):
            n = len(pattern)
            lps = [0] * n

            length = 0  # length of previous longest prefix suffix
            i = 1

            while i < n:
                # This is just moving left and right fingers to right. when found match.
                if pattern[i] == pattern[length]:
                    length += 1  # left finger
                    lps[i] = length
                    i += 1  # right finger
                else:
                    # lps 알고리즘에서 어려운 부분. fallback 할때 현재 prefix에서 가능한 가장 뒤쪽으로.
                    if length != 0:
                        length = lps[length - 1]  # fallback
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        comp_nums = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                comp_nums.append(1)
            elif nums[i] < nums[i-1]:
                comp_nums.append(-1)
            else:
                comp_nums.append(0)

        _lps = compute_lps(pattern)
        ans = 0

        i = 0  # pointer for text
        j = 0  # pointer for pattern

        while i < len(comp_nums):
            if comp_nums[i] == pattern[j]:
                i += 1
                j += 1

            if j == len(pattern):
                ans += 1
                j = _lps[j - 1]  # continue searching

            elif i < len(comp_nums) and comp_nums[i] != pattern[j]:
                if j != 0:
                    j = _lps[j - 1]
                else:
                    i += 1
        return ans
