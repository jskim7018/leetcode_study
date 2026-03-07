from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sorting 하면 매우 쉬움. 하지만 sorting 없이는?
        # heap으로 가능하긴 함. 하지만 사실상 sorting 한것 (heapsort)
        # 각 위치별로 갯수를 저장. 그리고 하나씩 증가하면서 구함.

        minim, maxim = min(0, min(nums)), max(nums)

        num_cnt = [0] * ((-minim) + maxim + 1)

        for num in nums:
            num_cnt[num + (-minim)] += 1

        curr_cnt = 0
        n = len(num_cnt)
        for i in range(n-1, -1, -1):
            curr_cnt += num_cnt[i]
            if k <= curr_cnt:
                return i - (-minim)

        return -1
