from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        ans = 0
        def calculate(s, e) -> int:
            nonlocal ans

            right = 0
            last_min_max = s-1
            maxims = set()
            minims = set()
            for i in range(s, e+1):
                if i != s:
                    if nums[i-1] == minK:
                        minims.remove(i-1)
                    if nums[i-1] == maxK:
                        maxims.remove(i-1)
                if nums[i] == minK:
                    minims.add(i)
                if nums[i] == maxK:
                    maxims.add(i)


                if nums[i] != minK and nums[i] != maxK:
                    continue
                if right < i:
                    right = i
                while right <= e and (len(minims) == 0 or len(maxims) == 0):
                    if right > i and nums[right]:
                        if nums[right] == minK:
                            minims.add(right)

                        if nums[right] == maxK:
                            maxims.add(right)
                    if len(minims) > 0 and len(maxims) > 0:
                        break
                    right += 1
                if len(minims) > 0 and len(maxims) > 0 and right <= e:
                    right_cnt = e-right+1
                    left_cnt = i-last_min_max
                    ans += right_cnt * left_cnt
                last_min_max = i

        l = 0
        nums.append(float('inf'))
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                if l <= i-1:
                    calculate(l,i-1)
                l = i+1

        return ans

# Chat GPT code.
# from typing import List
#
#
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         last_invalid = -1  # index of last element < minK or > maxK
#         last_min = -1  # index of last element == minK
#         last_max = -1  # index of last element == maxK
#
#         count = 0
#         for i, x in enumerate(nums):
#             # If x is out of [minK, maxK], no subarray can cross here
#             if x < minK or x > maxK:
#                 last_invalid = i
#
#             # Update last positions of minK and maxK
#             if x == minK:
#                 last_min = i
#             if x == maxK:
#                 last_max = i
#
#             # Number of valid subarrays ending at i is the number of possible starts:
#             # from last_invalid+1 up to min(last_min, last_max), if that’s ≥ last_invalid+1
#             valid_start_upto = min(last_min, last_max)
#             if valid_start_upto > last_invalid:
#                 count += (valid_start_upto - last_invalid)
#
#         return count
