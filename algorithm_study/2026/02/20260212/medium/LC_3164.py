from typing import List
from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # make counter with nums2[i] * k
        # factorize each nums1 then add counter[factor] to answer
        # 즉, nums2의 모든 숫자를 각각의 nums1에 해보는게 아니라 반대로 nums1의 숫자를 분해해서
        # nums2에 몇개 있는지 확인.

        counter = defaultdict(int)
        nums1_div_k = defaultdict(int)
        for num1 in nums1:
            if num1 % k == 0:
                nums1_div_k[num1//k] += 1
        for num2 in nums2:
            counter[num2] += 1

        if not nums1_div_k:
            return 0

        max_num1 = max(nums1_div_k)

        ans = 0
        for k, v in counter.items():
            for mult in range(k, max_num1 + 1, k):
                if mult in nums1_div_k:
                    ans += v * nums1_div_k[mult]

        return ans

# TODO: Study sieve method. how does it work???
# from typing import List
# from collections import Counter
#
# class Solution:
#     def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         freq2 = Counter(nums2)
#         freq1 = Counter()
#
#         # build freq1 only for valid nums1
#         for num in nums1:
#             if num % k == 0:
#                 freq1[num // k] += 1
#
#         if not freq1:
#             return 0
#
#         max_x = max(freq1)
#         ans = 0
#
#         # sieve over multiples
#         for b, cnt_b in freq2.items():
#             for multiple in range(b, max_x + 1, b):
#                 if multiple in freq1:
#                     ans += cnt_b * freq1[multiple]
#
#         return ans
