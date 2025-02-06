from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        ans = []
        for q in queries:
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                if (nums[q[1]] - q[0]) % 2 != 0:
                    even_sum += nums[q[1]]
                else:
                    even_sum += q[0]
            else:
                if (nums[q[1]] - q[0]) % 2 == 0:
                    even_sum -= (nums[q[1]] - q[0])
            ans.append(even_sum)

        return ans
