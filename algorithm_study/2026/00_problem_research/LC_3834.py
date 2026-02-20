from typing import List
from collections import deque
import heapq


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 큰게 되면 작은것들도 된다.
        # 왼쪽에서 부터 되는 것들을 늘려나가면서 구한다. 안되면 l을 움직인다.
        # 각각 되는 곳마다 (right 포함 모든 subarray) 갯수를 누적한다.
        # max, min은 어떻게 동적으로 유지? => heap+lazy deletion? segment tree도 가능한데 over engineering 일듯.
        # TODO: max, min O(n) dynamically calculate -> monotonic queue
        # TODO: 몇 없는 monotonic queue 문제. monotonic queue에 대해서 정확히 분석하자.
        # TODO: min, max 동적 유지시 유용하게 활용 가능.

        mono_max = deque()  # decreasing
        mono_min = deque()  # increasing

        n = len(nums)

        l = 0
        ans = 0
        for r in range(n):
            while mono_max and mono_max[-1] < nums[r]:
                mono_max.pop()
            while mono_min and mono_min[-1] > nums[r]:
                mono_min.pop()

            mono_max.append(nums[r])
            mono_min.append(nums[r])

            length = r - l + 1
            while (mono_max[0] - mono_min[0]) * length > k:
                if mono_max[0] == nums[l]:
                    mono_max.popleft()
                if mono_min[0] == nums[l]:
                    mono_min.popleft()
                l += 1
                length = r - l + 1

            ans += length

        return ans
