from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n-1):
            need = target - numbers[i]
            l = i+1
            r = n-1
            while l <= r:
                mid = (l+r)//2
                if numbers[mid] == need:
                    return [i+1, mid+1]
                elif numbers[mid] > need:
                    r = mid - 1
                else:
                    l = mid + 1

        return [0, 0]
