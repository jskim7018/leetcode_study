from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # TODO: O(n) Two pointer로 다시 해보기. 내가 왜 two pointer 방법을 못떠올렸는지 정확히 이해하자.
        ans = float('inf')
        for i in range(n):
            l = i
            r = n-1

            up_to = i
            while l <= r:
                mid = (l+r)//2
                if nums[i]*k >= nums[mid]:
                    up_to = mid
                    l = mid + 1
                else:
                    r = mid - 1
            ans = min(ans, n-(up_to - i + 1))

        return ans
