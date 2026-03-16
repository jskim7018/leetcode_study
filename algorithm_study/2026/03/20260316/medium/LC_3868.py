from collections import defaultdict


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        n = len(nums1)
        keys = set()
        for i in range(n):
            counter1[nums1[i]] += 1
            counter2[nums2[i]] += 1
            keys.add(nums1[i])
            keys.add(nums2[i])

        swaps = 0
        for k in keys:
            cnt1 = counter1[k]
            cnt2 = counter2[k]
            if (cnt1 + cnt2) % 2 != 0:
                return -1
            half = (cnt1+cnt2)//2
            swaps += abs(cnt1 - half)

        return swaps//2 + swaps % 2
