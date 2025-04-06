from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                nums_1_str = str(nums[i])
                nums_2_str = str(nums[j])
                if nums[i] == nums[j]:
                    ans += 1
                elif len(nums_1_str) == len(nums_2_str):
                    diff_1 = list()
                    diff_2 = list()
                    for k in range(len(nums_1_str)):
                        if nums_1_str[k] != nums_2_str[k]:
                            diff_1.append(nums_1_str[k])
                            diff_2.append(nums_2_str[k])
                    diff_1.sort()
                    diff_2.sort()
                    if diff_1 == diff_2 and len(diff_1) == 2:
                        ans += 1
                elif abs(len(nums_1_str) - len(nums_2_str)) >= 1:
                    if nums[i] > nums[j]:
                        larger = nums_1_str
                        smaller = nums_2_str
                    else:
                        larger = nums_2_str
                        smaller = nums_1_str

                    not_possible = False
                    cnt = 0
                    diff = abs(len(nums_1_str) - len(nums_2_str))
                    for k in range(len(smaller)-1, -1,-1):
                        if smaller[k] != larger[k+diff]:
                            if larger[k+diff] != '0':
                                not_possible = True
                                break
                            if cnt != 0:
                                not_possible = True
                                break
                            if smaller[k] != larger[0]:
                                not_possible = True
                                break
                            if larger[1:diff] != '0'*(diff-1):
                                not_possible = True
                                break
                            cnt = 1

                    if not not_possible and cnt == 1:
                        ans += 1

        return ans
