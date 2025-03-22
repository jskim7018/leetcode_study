from typing import List
import math

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        element_to_idx = dict()
        for i, e in enumerate(elements):
            if e not in element_to_idx:
                element_to_idx[e] = i

        ans = []
        for group in groups:
            minim_idx = float('inf')
            for i in range(1, math.ceil(group**0.5)+1):
                if group % i == 0:
                    j = group / i
                    if i in element_to_idx:
                        minim_idx = min(minim_idx, element_to_idx[i])
                    if j in element_to_idx:
                        minim_idx = min(minim_idx, element_to_idx[j])
            if minim_idx == float('inf'):
                ans.append(-1)
            else:
                ans.append(minim_idx)

        return ans

# TODO: analyze below code why it is nlogn
# faster code
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/solutions/6396012/python-beat-100-o-nlogn/
# class Solution:
#     def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
#         # each number => smallest index
#         mp = {}
#         max_num = max(groups)
#         for i, e in enumerate(elements):
#             num = e
#             # 优化
#             if e not in mp:
#                 while e <= max_num:
#                     if e not in mp:
#                         mp[e] = i
#                     e += num
#
#         res = []
#         for e in groups:
#             if e not in mp:
#                 res.append(-1)
#             else:
#                 res.append(mp[e])
#
#         return res
